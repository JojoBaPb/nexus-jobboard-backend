# Nexus Job Board Backend

This is the backend for the Nexus Job Board project. It provides RESTful APIs for user authentication, job postings, categories, companies, and job applications. Built with Django, Django REST Framework, and JWT authentication.

---

## Features

- User registration, login, logout, profile management
- JWT-based authentication (access & refresh tokens)
- CRUD APIs for Jobs, Categories, and Companies
- Job Applications linked to users & jobs
- Role-based permissions:
  - Admins can manage jobs, categories, companies, and applications
  - Regular users can browse jobs and apply
- API documentation with Swagger & ReDoc
- Deployed on Render

---

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Auth**: JWT (djangorestframework-simplejwt)
- **Docs**: drf-spectacular (Swagger, ReDoc)
- **Database**: PostgreSQL
- **Deployment**: Render

---

## Project Structure

core/ # Django project settings
users/ # User auth & profile management
jobs/ # Jobs, categories, companies
applications/ # Job applications linked to users & jobs


---

## Authentication

### Register
`POST /api/users/register/`

**Payload:**
json
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securepassword"
}

Login

POST /api/token/

Payload:

{
  "username": "johndoe",
  "password": "securepassword"
}

Response:

{
  "access": "<ACCESS_TOKEN>",
  "refresh": "<REFRESH_TOKEN>"
}

Refresh Token

POST /api/token/refresh/

 API Endpoints
Users
Method	Endpoint	Description
POST	/api/users/register/	Register a new user
POST	/api/token/	Login (obtain JWT)
POST	/api/token/refresh/	Refresh JWT
GET	/api/users/profile/	Get user profile
PUT	/api/users/profile/	Update user profile
POST	/api/users/change-password/	Change password
POST	/api/users/logout/	Logout (blacklist refresh token)
Jobs
Method	Endpoint	Description
GET	/api/jobs/	List all jobs
POST	/api/jobs/	Create a new job (Admin only)
GET	/api/jobs/{id}/	Retrieve job details
PUT	/api/jobs/{id}/	Update job (Admin only)
DELETE	/api/jobs/{id}/	Delete job (Admin only)
Categories
Method	Endpoint	Description
GET	/api/categories/	List categories
POST	/api/categories/	Create category (Admin only)
GET	/api/categories/{id}/	Get category details
PUT	/api/categories/{id}/	Update category (Admin only)
DELETE	/api/categories/{id}/	Delete category (Admin only)
Companies
Method	Endpoint	Description
GET	/api/companies/	List companies
POST	/api/companies/	Create company (Admin only)
GET	/api/companies/{id}/	Get company details
PUT	/api/companies/{id}/	Update company (Admin only)
DELETE	/api/companies/{id}/	Delete company (Admin only)
Applications
Method	Endpoint	Description
GET	/api/applications/	List all applications (Admin only)
POST	/api/applications/	Apply for a job (requires login)
GET	/api/applications/{id}/	Get details of a specific application
DELETE	/api/applications/{id}/	Withdraw application (owner or admin only)

Example Payload:

{
  "job": 2,
  "cover_letter": "I'm a great fit!"
}

 API Documentation

    Swagger UI: https://nexus-jobboard-backend.onrender.com/api/docs/swagger/

ReDoc: https://nexus-jobboard-backend.onrender.com/api/docs/redoc/

OpenAPI Schema: https://nexus-jobboard-backend.onrender.com/api/schema/

 Local Development

Clone the repo and set up locally:

git clone https://github.com/JojoBaPb/nexus-jobboard-backend
cd nexus-jobboard-backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

 Deployment

This backend is deployed on Render.
Start command:

bash -lc "python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn core.wsgi:application --bind 0.0.0.0:$PORT"

 ERD (Entity Relationship Diagram)

    Users

    Companies

    Jobs (linked to categories and companies)

    Applications (linked to users and jobs)

(ERD diagram included in project slides)

 Demo

Final deliverable includes:

    Slides covering features, ERD, tech stack

    Demo video showing:

        Register/login

        Admin creating jobs/categories

        User browsing & applying for jobs

        Swagger docs live

        Deployed app working


---
