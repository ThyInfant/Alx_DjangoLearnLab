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

## Posts Endpoints

GET /api/posts/
POST /api/posts/
GET /api/posts/{id}/
PUT /api/posts/{id}/
DELETE /api/posts/{id}/

Search:
GET /api/posts/?search=keyword

Pagination:
GET /api/posts/?page=1

## Comments Endpoints

GET /api/comments/
POST /api/comments/
GET /api/comments/{id}/
PUT /api/comments/{id}/
DELETE /api/comments/{id}/
