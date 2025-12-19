"""
FastAPI Task Management API - Starter Code

This is a basic structure to help you get started with your FastAPI application.
Complete the TODOs to build a full-featured task management API.

Run the application with: uvicorn starter-code:app --reload
Access the API documentation at: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI application
app = FastAPI(
    title="Task Management API",
    description="A simple REST API for managing tasks",
    version="1.0.0"
)

# TODO: Define the Task model using Pydantic
# Hint: Include fields for id (int), title (str), description (str), and completed (bool)
class Task(BaseModel):
    pass


# In-memory storage for tasks (will reset when server restarts)
tasks = []
next_task_id = 1


# Root endpoint
@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to the Task Management API!"}


# TODO: Implement POST /tasks to create a new task
# Hint: Use @app.post("/tasks", status_code=201) and return the created task


# TODO: Implement GET /tasks to retrieve all tasks
# Hint: Add optional query parameters for filtering (completed: bool, search: str)


# TODO: Implement GET /tasks/{task_id} to retrieve a specific task
# Hint: Raise HTTPException with status_code=404 if task not found


# TODO: Implement PUT /tasks/{task_id} to update a task
# Hint: Allow updating title, description, and completed status


# TODO: Implement DELETE /tasks/{task_id} to delete a task
# Hint: Return a success message after deletion


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
