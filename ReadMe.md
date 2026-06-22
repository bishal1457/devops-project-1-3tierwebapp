# Docker Deployment Todo App With webHook

This repository contains the source code and configuration files for deploying a Todo application using Docker and Docker Compose.

---

## Table of Contents

* [Project Structure](#project-structure)
* [Prerequisites](#prerequisites)
* [Setup Instructions](#setup-instructions)
* [Environment Variables Setup](#environment-variables-setup)
* [Running the Application](#running-the-application)
* [Scaling the Application](#scaling-the-application)
* [Contributing](#contributing)
* [License](#license)

---

## Project Structure

```text
docker-deployment-todoapp/
├── backend/
│   ├── src/
│   │   └── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── database/
│   ├── init.sql
│   └── Dockerfile
├── frontend/
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── scripts.js
│       └── styles.css
├── .env
├── nginx.conf
├── docker-compose.yml
└── README.md
```

---

## Prerequisites

Before you begin, ensure the following tools are installed on your system:

* Docker
* Docker Compose
* Git

Verify installation:

```bash
docker --version
docker-compose --version
git --version
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/<your-repository>.git
cd docker-deployment-todoapp
```

### 2. Create Environment Variables File

Create a `.env` file in the project root:

```bash
touch .env
```

For Windows PowerShell:

```powershell
New-Item .env -ItemType File
```

---

## Environment Variables Setup

Add the following variables to your `.env` file:

```env
POSTGRES_DB=your_database_name
POSTGRES_USER=your_database_user
POSTGRES_PASSWORD=your_database_password
```

### Example

```env
POSTGRES_DB=tododb
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin123
```

Docker Compose automatically loads variables from the `.env` file.

---

## Build and Run the Application

Start all services:

```bash
docker-compose -p mytodoapp up --build -d
```

Verify containers are running:

```bash
docker ps
```

---

## Running the Application

Once the containers are running, access the application using the following URLs:

### Through Nginx

```text
http://localhost
```

### Direct Flask Access

```text
http://localhost:5001
```

---

## Stopping the Application

To stop and remove all running containers:

```bash
docker-compose -p mytodoapp down
```

---

## Scaling the Application

You can scale individual services using Docker Compose.

Example: Scale the database service to 3 containers.

```bash
docker-compose -p mytodoapp up --scale database=3 -d
```

> **Note:** Ensure sufficient ports and system resources are available before scaling services.

---

## Useful Docker Commands

### View Running Containers

```bash
docker ps
```

### View Logs

```bash
docker-compose logs -f
```

### Restart Services

```bash
docker-compose restart
```

### Rebuild Containers

```bash
docker-compose up --build -d
```

---

## Contributing

Contributions are welcome.

### 1. Fork the Repository

Create your own copy of the repository.

### 2. Create a Feature Branch

```bash
git checkout -b feature-branch
```

### 3. Make Changes

Implement your feature or bug fix.

### 4. Commit Changes

```bash
git add .
git commit -m "Add new feature"
```

### 5. Push Changes

```bash
git push origin feature-branch
```

### 6. Open a Pull Request

Submit a Pull Request for review.

---

## License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.

---

## Author

Developed as part of a Docker and DevOps learning project demonstrating:

* Multi-container application deployment
* Docker Compose orchestration
* Nginx reverse proxy configuration
* PostgreSQL database integration
* Flask backend services
* Frontend application deployment
