# Social Media API

A Django REST API for user authentication and basic social features.

## Setup

1. Clone the repository
2. Install dependencies:
   pip install django djangorestframework
3. Run migrations:
   python manage.py migrate
4. Start server:
   python manage.py runserver

## Authentication

This API uses Token Authentication.

### Register

POST /api/accounts/register/

### Login

POST /api/accounts/login/

### Profile

GET /api/accounts/profile/
Header: Authorization: Token <your_token>

## User Model

The custom user model extends AbstractUser and includes:

- bio
- profile_picture
- followers system
