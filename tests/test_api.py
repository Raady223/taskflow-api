from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "TaskFlow API is running"
    }


def test_register_login_and_project_task_flow():
    # Register a new test user
    register_response = client.post(
        "/users/register",
        json={
            "username": "testuser123",
            "email": "testuser123@example.com",
            "password": "TestPassword123!"
        }
    )

    assert register_response.status_code in [201, 400]

    # Login
    login_response = client.post(
        "/users/login",
        data={
            "username": "testuser123@example.com",
            "password": "TestPassword123!"
        }
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    headers = {
        "Authorization": f"Bearer {token}"
    }

    # Create project
    project_response = client.post(
        "/projects/",
        json={
            "title": "Automated Test Project",
            "description": "Created by pytest"
        },
        headers=headers
    )

    assert project_response.status_code == 201

    project = project_response.json()
    project_id = project["id"]

    assert project["title"] == "Automated Test Project"

    # Get projects
    get_projects_response = client.get(
        "/projects/",
        headers=headers
    )

    assert get_projects_response.status_code == 200

    # Create task
    task_response = client.post(
        f"/tasks/project/{project_id}",
        json={
            "title": "Automated Test Task",
            "description": "Created during automated testing",
            "status": "todo"
        },
        headers=headers
    )

    assert task_response.status_code == 201

    task = task_response.json()
    task_id = task["id"]

    assert task["status"] == "todo"
    assert task["project_id"] == project_id

    # Update task
    update_task_response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "Automated Test Task",
            "description": "Updated during automated testing",
            "status": "done"
        },
        headers=headers
    )

    assert update_task_response.status_code == 200
    assert update_task_response.json()["status"] == "done"

    # Delete task
    delete_task_response = client.delete(
        f"/tasks/{task_id}",
        headers=headers
    )

    assert delete_task_response.status_code == 204

    # Delete project
    delete_project_response = client.delete(
        f"/projects/{project_id}",
        headers=headers
    )

    assert delete_project_response.status_code == 204


def test_protected_projects_without_token():
    response = client.get("/projects/")

    assert response.status_code == 401