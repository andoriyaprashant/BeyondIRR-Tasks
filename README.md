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
**Endpoint:** `/api/token/`  
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
### Example 

```json
{
  "email": "demo4@gmail.com",
  "password": "prashant810"
}
```
### Response 

```json
{
    "refresh": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNDA4MzE1MSwiaWF0IjoxNzIzOTk2NzUxLCJqdGkiOiJiNWI4MzRhM2M5ZTQ0NGU3YWNiNDIyNjQwMzgxY2UwMCIsInVzZXJfaWQiOjF9.LY6u2SSEbM8tf6_tm5RNwJ9ik4FBwf19yT3WGNjUEvR8av55vrQCVptsKpIp9GBETEy_-4C9j_cRvVyClTIxtJlvJpLlTyHfxo8h2ojdBlA3exc-gJd6yzIhSAlDWwPaQpgVgqzKmovYoqZB56J4wkpAhfPld-ZfCSbrL9q2x-dggB9AQPgSUAQTiyRJI8bFvQ1pDHN4MPGXNzNLITt7gGIALt19WoTZrV6zZDFevffbQt5dE9vuBPq1yg3Gxp83PJhT-mjQHQnSTB92IUAZJZ6d6mSzHuij1x_feMT32eftWvSocVLYTZQgzS36xFZ8EXkvpLDnGobaS6t1k3lKKA",
    "access": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzOTk3MDUxLCJpYXQiOjE3MjM5OTY3NTEsImp0aSI6Ijc3NDk4MWIxYTE1OTRkZWRhNmU3MzYyZTM1MGRjZTZhIiwidXNlcl9pZCI6MX0.OANS_zTT8dtAs2gyzeMKFc8B7DeG1c8fgb7YeM0QQW95IJJbUnfghw11DxGGb7eLnxU1DGncEa1x2z1UCOOxd3A3OAvcAYJHCR6XngpE3EVGnjfsuRao7zUP9WOsFonjpNJjtnGZevsDge5_DApEInHZGFRXj5YaG5-BUH2jW5b6soZLT4GLoQayK6f0cff_wTfPBFgzytGGrgQcdnfnFFFiQZfGAB4rlKPu_t7QarcGi8oolU4G1M8-QsUSs7hWWWc_0-pXXfYAYed7-27iOXasCFAMfYhctkNDl0q6Js2nIFoD3fIn4iWvaFWJPjsJUuAdWPDajJuhVG3SWfQQUA"
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

## Comprehensive Test Suite

### Models

- **UserModelTest**: Tests the functionality of the custom `User` model.
  - `test_user_creation`: Verifies user creation and attribute assignment.
  - `test_string_representation`: Checks the string representation of the user.

### Serializers

- **UserSerializerTest**: Tests the `UserSerializer` for correct data serialization.
  - `test_user_serializer`: Validates that serialized data matches expected values.
  
- **LoginSerializerTest**: Tests the `LoginSerializer` for login validation.
  - `test_login_serializer`: Ensures the serializer correctly validates login credentials.

### Views

- **LoginAPITest**: Tests API views related to authentication and protected resources.
  - `test_login_success`: Verifies successful login returns access and refresh tokens.
  - `test_login_failure`: Checks response for failed login attempts.
  - `test_protected_view`: Ensures access to protected views is restricted and returns correct responses.
  - `test_protected_view_without_token`: Validates access denial for protected views without a token.

### Run Unit Tests

```bash
python manage.py test
```

### Run Tests with Coverage

```bash
pytest --cov=api
```
