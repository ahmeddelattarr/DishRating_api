# API Documentation

This document provides an overview of the API endpoints and their associated permissions.

## Base URL

The base URL for all API endpoints is not specified in the provided configuration. Ensure you prepend the correct base URL to all endpoints listed below.

## Endpoints

### User Management

#### 1. User Registration
- **Endpoint**: `/register/`
- **Method**: POST
- **Permissions**: AllowAny
- **Description**: Register a new user
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string",
   
  }
  ```
- **Response**: Returns a token for the newly created user

#### 2. User Listing (Disabled)
- **Endpoint**: `/register/`
- **Method**: GET
- **Permissions**: AllowAny
- **Description**: This endpoint is disabled and returns an error message

#### 3. User Login
- **Endpoint**: `/login/`
- **Method**: POST
- **Permissions**: AllowAny
- **Description**: Authenticate a user and receive a token
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response**: Returns a token for the authenticated user
- **Error Responses**:
  - If username or password is missing: 400 Bad Request
  - If credentials are invalid: 402 unauthorized

### Meal Management

#### 1. List All Meals
- **Endpoint**: `/meals/`
- **Method**: GET
- **Permissions**: Not specified (assumed to be open)
- **Description**: Retrieve a list of all meals

#### 2. Create a Meal
- **Endpoint**: `/meals/`
- **Method**: POST
- **Permissions**: Not specified (assumed to require authentication)
- **Description**: Create a new meal

#### 3. Rate a Meal
- **Endpoint**: `/meals/{meal_id}/rate_meal/`
- **Method**: POST
- **Permissions**: IsAuthenticated
- **Description**: Rate a specific meal
- **Request Body**:
  ```json
  {
    "stars": integer
  }
  ```
- **Response**: Returns the created or updated rating

### Rating Management

#### 1. List All Ratings
- **Endpoint**: `/ratings/`
- **Method**: GET
- **Permissions**: IsAuthenticated
- **Description**: Retrieve a list of all ratings

#### 2. Create a Rating
- **Endpoint**: `/ratings/`
- **Method**: POST
- **Permissions**: IsAuthenticated
- **Description**: Create a new rating

## Authentication

This API uses token-based authentication. To authenticate, include the token in the Authorization header of your requests:

```
Authorization: Token <your-token-here>
```

To obtain a token, use the login endpoint described above.

## Permissions

- **AllowAny**: No authentication is required
- **IsAuthenticated**: User must be authenticated (valid token required)

## Notes

1. The user listing endpoint is intentionally disabled for security reasons.
2. Make sure to include the authentication token in the header for endpoints requiring authentication.
3. When rating a meal, ensure you're using the correct meal ID in the URL.
4. The API uses Django Rest Framework's DefaultRouter, which provides additional endpoints for detail views, updates, and deletions that are not explicitly listed here.

For any issues or further clarification, please contact the API administrator.
