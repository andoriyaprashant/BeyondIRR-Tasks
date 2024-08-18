## Project Structure

- **`demodjango/`**: Main project directory
  - **`demodjango/`**: Project settings and configuration
  - **`api/`**: Django app containing views, serializers, and models
- **`requirements.txt`**: List of dependencies

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/user/BeyondIRR-Tasks.git
```
### Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
### Install Dependencies

```bash
pip install -r requirements.txt
```
### Apply Migrations

```bash
python manage.py migrate
```
### Create a Superuser (optional for accessing Django admin)

```bash
python manage.py createsuperuser
```
### Start the Development Server

```bash
python manage.py runserver
```

# API Documentation

## Authentication

### Login
**Endpoint:** `/login/`  
**Method:** POST  

**Request Format:** JSON  
**Request Body:**

```json
{
  "email": "user@example.com",
  "password": "password"
}
```
### Response 

```json
{
  "status": "success",
  "refresh": "<refresh-token>",
  "access": "<access-token>"
}
```

### Error (Invalid Credentials):

```json
{
  "status": "error",
  "message": "Invalid credentials"
}
```
## Protected Endpoint

### Access Protected Resource

**Endpoint:** `/api/protected/`  
**Method:** GET  

**Headers:**

```makefile
Authorization: Bearer <access-token>
```

### Response 

- Success

```json
{
  "message": "This is a protected view only accessible to authenticated users."
}
```

### Error

```json
{
  "detail": "Authentication credentials were not provided."
}
```