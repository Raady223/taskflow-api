# TaskFlow API

TaskFlow API is a backend project and task management system built with FastAPI, PostgreSQL, SQLAlchemy, JWT authentication, Pytest, and Docker.

The project demonstrates backend development concepts commonly used in real-world software engineering, including authentication, database relationships, protected routes, CRUD operations, validation, automated testing, and containerization.

## Features

- User registration
- Secure password hashing with bcrypt
- User login
- JWT authentication
- Protected API routes
- Create, view, update, and delete projects
- Create, view, update, and delete tasks
- Tasks linked to projects
- User ownership protection
- Input validation with Pydantic
- PostgreSQL database
- SQLAlchemy ORM
- Automated API testing with Pytest
- Docker and Docker Compose support
- Interactive Swagger API documentation

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT
- bcrypt
- Pytest
- Docker
- Docker Compose
- Uvicorn

## Project Structure

taskflow-api/
│
├── app/
│   ├── routers/
│   │   ├── users.py
│   │   ├── projects.py
│   │   └── tasks.py
│   │
│   ├── auth.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── tests/
│   └── test_api.py
│
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

## Authentication

TaskFlow uses JWT-based authentication.

Users register with a username, email, and password. Passwords are hashed before being stored in PostgreSQL.

After login, the API generates a JWT access token. Protected routes require the token using the Bearer authentication scheme.

## API Endpoints

### Users

POST /users/register
POST /users/login

### Projects

POST   /projects/
GET    /projects/
GET    /projects/{project_id}
PUT    /projects/{project_id}
DELETE /projects/{project_id}

### Tasks

POST   /tasks/project/{project_id}
GET    /tasks/project/{project_id}
GET    /tasks/{task_id}
PUT    /tasks/{task_id}
DELETE /tasks/{task_id}

## Task Status Validation

Tasks support the following statuses:

todo
in_progress
done

Invalid values are automatically rejected by Pydantic validation.

## Running With Docker

Build and start the API and PostgreSQL database:

docker compose up --build

Then open:

http://127.0.0.1:8000/docs

Swagger UI provides interactive documentation for testing the API.

To stop the containers:

docker compose down

## Running Tests

Run the automated tests with:

python -m pytest

The tests verify core API functionality including authentication, protected routes, project creation, task creation, task updates, and deletion.

## Environment Variables

Copy `.env.example` to `.env` and configure:

DATABASE_URL
SECRET_KEY
ACCESS_TOKEN_EXPIRE_MINUTES

The real `.env` file is excluded from Git using `.gitignore`.

## What I Learned

Through this project, I practiced:

- Designing REST APIs with FastAPI
- Connecting Python applications to PostgreSQL
- Using SQLAlchemy ORM models and relationships
- Implementing JWT authentication
- Hashing and verifying passwords securely
- Protecting routes based on authenticated users
- Performing CRUD operations
- Implementing ownership-based access control
- Validating API input using Pydantic
- Writing automated tests with Pytest
- Containerizing applications using Docker
- Running multi-container applications with Docker Compose
- Managing application configuration with environment variables