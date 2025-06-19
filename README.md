# Simple Social Media API

A FastAPI-based social media API with user authentication and post management.

## Features

- User registration and authentication with JWT tokens
- Secure password hashing with bcrypt
- Post creation, reading, and deletion
- User-specific post management
- CORS enabled for frontend integration

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

### Authentication

- `POST /register/` - Register a new user
- `POST /login/` - Login and get access token
- `GET /users/me/` - Get current user info (requires authentication)

### Users

- `GET /users/` - Get all users
- `GET /users/{user_id}` - Get specific user

### Posts

- `POST /posts/` - Create a new post (requires authentication)
- `GET /posts/` - Get all posts
- `GET /posts/my/` - Get current user's posts (requires authentication)
- `GET /posts/{post_id}` - Get specific post
- `DELETE /posts/{post_id}` - Delete a post (requires authentication, owner only)

## Usage Examples

### 1. Register a new user
```bash
curl -X POST "http://localhost:8000/register/" \
  -H "Content-Type: application/json" \
  -d '{"username": "john_doe", "email": "john@example.com", "password": "secretpassword"}'
```

### 2. Login and get token
```bash
curl -X POST "http://localhost:8000/login/" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=john_doe&password=secretpassword"
```

### 3. Create a post (with authentication)
```bash
curl -X POST "http://localhost:8000/posts/" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"content": "Hello, world!", "image_url": "https://example.com/image.jpg"}'
```

### 4. Get current user's posts
```bash
curl -X GET "http://localhost:8000/posts/my/" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Security Notes

- Change the `SECRET_KEY` in `app/auth.py` for production use
- The API uses bcrypt for password hashing
- JWT tokens expire after 30 minutes
- All sensitive endpoints require Bearer token authentication

## Database

The application uses SQLite by default. The database file will be created automatically when you first run the application.