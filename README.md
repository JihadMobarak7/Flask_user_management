# Flask_user_management

A simple RESTful API for managing user data using Flask and SQLite. This application supports basic CRUD operations: Create, Read, Update, and Delete users.

## Project Overview

This API allows for:
- Creating a new user.
- Fetching all users or a specific user by ID.
- Updating user details.
- Deleting a user by ID.

## Setup Instructions

### Prerequisites

- Python 3.x
- Git
- Postman (for testing)

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/JihadMobarak7/Flask_user_management.git
   cd Flask_user_management

## API Endpoints

| Endpoint                       | HTTP Method | Description                         |
|--------------------------------|-------------|-------------------------------------|
| `/api/users`                   | GET         | Retrieve all users                  |
| `/api/users/<user_id>`         | GET         | Retrieve a specific user by ID      |
| `/api/users/add`               | POST        | Add a new user                      |
| `/api/users/update`            | PUT         | Update an existing user             |
| `/api/users/delete/<user_id>`  | DELETE      | Delete a user by ID                 |
