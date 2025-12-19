# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build modern, high-performance REST APIs using the FastAPI framework. You will create a complete API with CRUD operations, request validation, and proper HTTP responses.

## 📝 Tasks

### 🛠️ Set Up FastAPI Application

#### Description
Create a basic FastAPI application with a welcome endpoint and proper project structure. Install FastAPI and its dependencies, then create your first API endpoint.

#### Requirements
Completed program should:

- Install FastAPI and uvicorn using pip
- Create a main application file (main.py)
- Define a root endpoint (`/`) that returns a welcome message
- Run the application using uvicorn
- Access the automatic API documentation at `/docs`


### 🛠️ Build a Task Management API

#### Description
Create a RESTful API for managing tasks. Implement all CRUD (Create, Read, Update, Delete) operations with proper HTTP methods and status codes.

#### Requirements
Completed program should:

- Define a Task model using Pydantic with fields: id, title, description, completed
- Implement POST `/tasks` to create new tasks
- Implement GET `/tasks` to retrieve all tasks
- Implement GET `/tasks/{task_id}` to retrieve a specific task
- Implement PUT `/tasks/{task_id}` to update a task
- Implement DELETE `/tasks/{task_id}` to delete a task
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Include request validation and error handling


### 🛠️ Add Query Parameters and Filtering

#### Description
Enhance your API with query parameters to filter and search tasks. Learn how to accept optional parameters and use them to customize API responses.

#### Requirements
Completed program should:

- Add optional query parameter `completed` to filter tasks by completion status
- Add optional query parameter `search` to search tasks by title or description
- Return filtered results when query parameters are provided
- Return all tasks when no query parameters are specified
- Test filtering functionality using the interactive API docs
