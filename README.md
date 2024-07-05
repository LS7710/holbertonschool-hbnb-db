
# HBnB Evolution - Enhanced

This project is a fork of the [hbnb_evolution](https://github.com/jhonaRiver/hbnb_evolution) repository.

## Changes Made

### 1. Integration of SQLAlchemy
- Added `Flask-SQLAlchemy` and `SQLAlchemy` to `requirements.txt`.
- Initialized SQLAlchemy in the Flask application (`hbnb.py`).
- Refactored existing models to use SQLAlchemy ORM.

### 2. Configurable Database Selection
- Created a dynamic database configuration system using environment variables.
- Modified application configuration to support SQLite for development and PostgreSQL for production.

### 3. Implemented Authentication with JWT
- Added `Flask-JWT-Extended` and `flask-bcrypt` to `requirements.txt`.
- Configured JWT in the Flask application (`hbnb.py`).
- Created a login endpoint to issue JWTs.
- Updated the `User` model to handle password hashing and role management.

### 4. Database Schema Design and Migration
- Designed a database schema and created SQL scripts for database initialization.
- Set up Alembic for managing database migrations.

### 5. Implemented Role-Based Access Control
- Updated the login process to include role information in JWTs.
- Secured API endpoints based on user roles (admin and non-admin).

### 6. Updated Docker Configuration
- Modified the Dockerfile to include necessary dependencies.
- Configured environment variables for database connections and JWT settings.
- Created a `docker-compose.yml` file for setting up the application with PostgreSQL.

## Installation
1. Clone the repository.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up the environment variables in a `.env` file.
4. Initialize the database:
   ```
   flask db upgrade
   ```
5. Run the application:
   ```
   flask run
   ```
6. Alternatively, use Docker to build and run the application:
   ```
   docker-compose up --build
   ```
