pipeline {
    agent any

    environment {
        APP_HOST   = "vagrant@192.168.56.102"
        APP_IP     = "192.168.56.102"
        DEPLOY_DIR = "/home/ubuntu/todoapp"
        COMPOSE    = "docker compose -p mytodoapp"
    }

    // Add this triggers block to listen for git webhooks
   // triggers {
     //   githubPush() // Use upstream() or gitlab() if not using GitHub
    }

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Test (backend)') {
            steps {
                sh '''
                    cd backend
                    python3 -m py_compile $(find src -name "*.py")
                '''
            }
        }

        stage('Deploy to app server') {
            steps {
                sshagent(['app-server-ssh']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no ${APP_HOST} "mkdir -p ${DEPLOY_DIR}"
                        rsync -az --delete --exclude venv --exclude .git \
                            -e "ssh -o StrictHostKeyChecking=no" \
                            ./ ${APP_HOST}:${DEPLOY_DIR}/
                    '''
                    withCredentials([file(credentialsId: 'todo-env', variable: 'ENV_FILE')]) {
                        sh 'scp -o StrictHostKeyChecking=no "$ENV_FILE" ${APP_HOST}:${DEPLOY_DIR}/.env'
                    }
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
                    sleep 20
                    code=$(curl -s -o /dev/null -w "%{http_code}" http://${APP_IP}:8080/)
                    echo "Homepage returned HTTP $code"
                    test "$code" = "200"
                '''
            }
        }
    }

    post {
        success { echo "Deployed. App live at http://${APP_IP}:8080/" }
        failure { echo "Failed — check the stage logs above" }
    }
}
