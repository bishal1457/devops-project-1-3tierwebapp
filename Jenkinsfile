pipeline {
    agent any

    environment {
        APP_HOST   = "deploy@10.0.0.20"      // <-- your app server user@ip
        APP_IP     = "10.0.0.20"
        DEPLOY_DIR = "/home/deploy/todoapp"
        COMPOSE    = "docker-compose -p mytodoapp"   // use 'docker compose' if on v2
    }

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Test (backend)') {
            steps {
                sh '''
                    cd backend
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    # basic gate: every .py file must compile cleanly
                    python -m py_compile $(find src -name "*.py")
                    # when you add real tests:  pytest -q
                '''
            }
        }

        stage('Deploy to app server') {
            steps {
                sshagent(['app-server-ssh']) {
                    // 1. push the code
                    sh '''
                        ssh -o StrictHostKeyChecking=no ${APP_HOST} "mkdir -p ${DEPLOY_DIR}"
                        rsync -az --delete --exclude venv --exclude .git \
                            ./ ${APP_HOST}:${DEPLOY_DIR}/
                    '''
                    // 2. push the real .env (stored as a Jenkins secret file)
                    withCredentials([file(credentialsId: 'todo-env', variable: 'ENV_FILE')]) {
                        sh 'scp -o StrictHostKeyChecking=no "$ENV_FILE" ${APP_HOST}:${DEPLOY_DIR}/.env'
                    }
                    // 3. build + run everything on the app server
                    sh '''
                        ssh -o StrictHostKeyChecking=no ${APP_HOST} "
                            cd ${DEPLOY_DIR} &&
                            ${COMPOSE} up --build -d &&
                            ${COMPOSE} ps
                        "
                    '''
                }
            }
        }

        stage('Smoke test') {
            steps {
                sh '''
                    sleep 8
                    code=$(curl -s -o /dev/null -w "%{http_code}" http://${APP_IP}/)
                    echo "Homepage returned HTTP $code"
                    test "$code" = "200"
                '''
            }
        }
    }

    post {
        success { echo "Deployed. App live at http://${APP_IP}/" }
        failure { echo "Failed — check the stage logs above" }
    }
}
