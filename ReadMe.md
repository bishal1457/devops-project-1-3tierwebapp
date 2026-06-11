# Docker Deployment Todo App

This repository contains the source code and configuration files for deploying a Todo application using Docker and Docker Compose.

## Table of Contents

- Project Structure
- Prerequisites
- Setup Instructions
- Environment Variables Setup
- Running the Application
- Contributing
- License

## Project Structure

```
docker-deployment-todoapp/
├── backend/
│   ├── src/
│   │   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
├── database/
│   ├── init.sql
│   ├── Dockerfile
├── frontend/
│   ├── templates/
│   │   ├── index.html
│   ├── static/
│   │   ├── scripts.js
│   │   ├── styles.css
├── .env
├── nginx.conf
├── docker-compose.yml
├── README.md

```

## Prerequisites

Before you begin, ensure you have met the following requirements:


- Docker
- Docker Compose


## Setup Instructions

1. **Clone the repository:**

    ```sh
    git clone https://github.com/vidit-khare/docker-deployment-todoapp.git
    ```

    ```sh
    cd docker-deployment-todoapp
    ```

## Environment Variables Setup

1. **Define Environment Variables**

This project uses a `.env` file to manage environment variables. Follow these steps to set up your environment variables:

- **Create a `.env` file in the root directory of the project:**

    ```sh
    touch .env
    ```

- **Add your environment variables to the `.env` file:** 

    **Note:** Setup variable values as per your requirement. The below config shows placeholder values.

    ```env
    POSTGRES_DB=your_database_name
    POSTGRES_USER=your_database_user
    POSTGRES_PASSWORD=your_database_password
    ```

#### Using Environment Variables in Docker Compose

Docker Compose will automatically load the variables from the `.env` file. Ensure your `docker-compose.yml` file references these variables:


3. **Build and run the Docker containers using Docker Compose:**

    ```sh
    docker-compose -p mytodoapp up --build -d
    ```

## Running the Application

This setup uses nginx as web server and hence you can reach your application on localhost at port 80. The other way is using flask url which is running on port 5001.

**Endpoints-** Once the containers are running, you can access the Todo application by navigating to below urls in your web browser.


`http://localhost`

`http://localhost:5001`


To stop the running containers, use the following command:

```sh
docker-compose -p mytodoapp down
```

## Scaling the Application

You can scale your application by using --scale flag.

Scale specific service for eg. database/

    ```sh
     docker-compose -p mytodoapp up --scale database=3 -d
    ```

**Note:** Make sure the number of ports are available while scaling the application otherwise update docker-compose to cater for more ports for the service you want to scale.

## Contributing

Contributions are always welcome! Please follow these steps to contribute:

1. **Fork the repository.**
2. **Create a new branch:**

    ```sh
    git checkout -b feature-branch
    ```

3. **Make your changes.**
4. **Commit your changes:**

    ```sh
    git commit -m 'Add some feature'
    ```

5. **Push to the branch:**

    ```sh
    git push origin feature-branch
    ```

6. **Open a pull request.**

## License

This project is licensed under the MIT License. See the LICENSE file for details.
