# Flask Authentication Project

A simple Flask application demonstrating authentication, SQLAlchemy ORM, and a REST API. **Links & Resources**:

- [Getting Started with Flask](https://app-generator.dev/docs/technologies/flask/index.html)
- [Flask Cheatsheet](https://app-generator.dev/docs/technologies/flask/cheatsheet.html)
- [Database Migrations in Flask](https://app-generator.dev/docs/technologies/flask/db-migrations.html)

## Features

- User authentication (login/register/logout)
- Public and protected routes
- SQLite database with SQLAlchemy ORM
- REST API endpoint for users
- Bootstrap-styled templates

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix or MacOS:
```bash
source venv/bin/activate
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python run.py
```

## Routes

- `/` - Public homepage
- `/private` - Protected route (requires login)
- `/api/users` - API endpoint listing all users
- `/login` - User login
- `/register` - User registration
- `/logout` - User logout

## API Usage

Get list of all users:
```bash
curl http://localhost:5000/api/users
```

## Security Note

This is a demonstration project. In a production environment, you should:
- Use a proper secret key
- Enable HTTPS
- Implement proper password validation
- Add rate limiting
- Use environment variables for sensitive data
