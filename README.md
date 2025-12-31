# 🎬 Movie Rating System

A robust RESTful API for managing movies and user ratings, built with modern Python technologies following clean architecture principles.

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [API Documentation](#-api-documentation)
- [Getting Started](#-getting-started)
- [Database](#-database)
- [Testing](#-testing)
- [Logging](#-logging)
- [Team](#-team)

---

## 🎯 Overview

Movie Rating System is a backend API that allows users to browse movies, view detailed information, and submit ratings. The system is designed with scalability and maintainability in mind, following industry best practices for RESTful API design.

### Key Highlights

- **1000+ Real Movies** from TMDB dataset with actual metadata
- **Clean 3-Layer Architecture** (Controller → Service → Repository)
- **Comprehensive Filtering** by title, genre, and release year
- **Real-time Rating Aggregation** with automatic average calculation
- **Production-Ready Docker Setup** with health checks

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎥 **Movie Management** | Full CRUD operations for movies |
| ⭐ **Rating System** | Submit and aggregate user ratings (1-10 scale) |
| 🔍 **Advanced Search** | Filter by title, genre, release year |
| 📄 **Pagination** | Efficient data retrieval with customizable page sizes |
| 🎭 **Genre Support** | Multi-genre assignment for movies |
| 🎬 **Director Info** | Linked director information with movies |
| 📝 **Logging** | Comprehensive request/response logging |
| 🐳 **Docker Ready** | One-command deployment with Docker Compose |

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| **Language** | Python 3.12 |
| **Framework** | FastAPI |
| **Database** | PostgreSQL 16 |
| **ORM** | SQLAlchemy 2.x |
| **Migration** | Alembic |
| **Validation** | Pydantic v2 |
| **Package Manager** | Poetry |
| **Containerization** | Docker & Docker Compose |
| **API Documentation** | Swagger UI (OpenAPI 3.0) |

---

## 🏗 Architecture

The project follows a **3-Layer Architecture** pattern for clean separation of concerns:

```
┌─────────────────────────────────────────────────────────────┐
│                      Client Request                         │
└─────────────────────────┬───────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                   Controller Layer                          │
│         (API Endpoints, Request/Response Handling)          │
│                  app/controllers/                           │
└─────────────────────────┬───────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                    Service Layer                            │
│            (Business Logic, Validation)                     │
│                   app/services/                             │
└─────────────────────────┬───────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                  Repository Layer                           │
│           (Data Access, Database Queries)                   │
│                 app/repositories/                           │
└─────────────────────────┬───────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                    PostgreSQL Database                      │
└─────────────────────────────────────────────────────────────┘
```

### Benefits of This Architecture

- **Separation of Concerns**: Each layer has a single responsibility
- **Testability**: Easy to unit test each layer independently
- **Maintainability**: Changes in one layer don't affect others
- **Scalability**: Easy to extend and modify

---

## 📁 Project Structure

```
Movie-Rating-System/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── config.py               # Configuration settings
│   ├── logging_config.py       # Logging configuration
│   │
│   ├── controllers/            # API Layer
│   │   ├── __init__.py
│   │   └── movie_controller.py # Movie & Rating endpoints
│   │
│   ├── services/               # Business Logic Layer
│   │   ├── __init__.py
│   │   ├── movie_service.py    # Movie business logic
│   │   └── rating_service.py   # Rating business logic
│   │
│   ├── repositories/           # Data Access Layer
│   │   ├── __init__.py
│   │   ├── base.py             # Base repository pattern
│   │   ├── movie_repository.py
│   │   ├── rating_repository.py
│   │   ├── director_repository.py
│   │   └── genre_repository.py
│   │
│   ├── models/                 # SQLAlchemy Models
│   │   ├── __init__.py
│   │   ├── base.py             # Base model with timestamps
│   │   ├── movie.py
│   │   ├── director.py
│   │   ├── genre.py
│   │   ├── movie_genre.py      # Many-to-Many bridge table
│   │   └── movie_rating.py
│   │
│   ├── schemas/                # Pydantic Schemas
│   │   ├── __init__.py
│   │   ├── base.py             # Base response schemas
│   │   ├── movie.py
│   │   ├── director.py
│   │   ├── genre.py
│   │   └── rating.py
│   │
│   ├── exceptions/             # Custom Exceptions
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── http_exceptions.py
│   │
│   └── db/                     # Database Configuration
│       ├── __init__.py
│       └── database.py
│
├── alembic/                    # Database Migrations
│   ├── versions/
│   │   └── 086a3e8677e0_create_initial_tables.py
│   ├── env.py
│   └── script.py.mako
│
├── scripts/                    # Utility Scripts
│   ├── seeddb.sql              # Database seeding script
│   └── seed_check.py           # Seed verification script
│
├── alembic.ini                 # Alembic configuration
├── docker-compose.yml          # Docker Compose configuration
├── Dockerfile                  # Docker image definition
├── pyproject.toml              # Poetry dependencies
├── poetry.lock                 # Locked dependencies
├── .env.example                # Environment variables template
├── .gitignore
└── README.md
```

---

## 📚 API Documentation

### Base URL

```
http://localhost:8000/api/v1
```

### Interactive Documentation

Once the server is running, access the Swagger UI:

```
http://localhost:8000/docs
```

### Endpoints Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/movies` | List movies with pagination & filters |
| `GET` | `/movies/{id}` | Get movie details |
| `POST` | `/movies` | Create a new movie |
| `PUT` | `/movies/{id}` | Update a movie |
| `DELETE` | `/movies/{id}` | Delete a movie |
| `POST` | `/movies/{id}/ratings` | Submit a rating |

---

### 📖 Detailed API Reference

#### 1. List Movies

```http
GET /api/v1/movies
```

**Query Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `page` | integer | 1 | Page number (min: 1) |
| `page_size` | integer | 10 | Items per page (max: 100) |
| `title` | string | - | Filter by title (partial match, case-insensitive) |
| `release_year` | integer | - | Filter by exact release year |
| `genre` | string | - | Filter by genre name (partial match) |

**Example Request:**

```bash
curl -X GET "http://localhost:8000/api/v1/movies?page=1&page_size=10&genre=Action"
```

**Example Response:**

```json
{
  "status": "success",
  "data": {
    "page": 1,
    "page_size": 10,
    "total_items": 245,
    "items": [
      {
        "id": 1,
        "title": "Star Wars",
        "release_year": 1977,
        "director": {
          "id": 816,
          "name": "George Lucas"
        },
        "genres": ["Science Fiction", "Adventure", "Action"],
        "average_rating": 5.9,
        "ratings_count": 31
      }
    ]
  }
}
```

---

#### 2. Get Movie Details

```http
GET /api/v1/movies/{movie_id}
```

**Example Response:**

```json
{
  "status": "success",
  "data": {
    "id": 1,
    "title": "Star Wars",
    "release_year": 1977,
    "director": {
      "id": 816,
      "name": "George Lucas",
      "birth_year": null,
      "description": "Imported from TMDB credits as Director"
    },
    "genres": ["Science Fiction", "Adventure", "Action"],
    "cast": "Mark Hamill, Harrison Ford, Carrie Fisher",
    "average_rating": 5.9,
    "ratings_count": 31
  }
}
```

---

#### 3. Create Movie

```http
POST /api/v1/movies
```

**Request Body:**

```json
{
  "title": "New Movie",
  "director_id": 1,
  "release_year": 2025,
  "cast": "Actor One, Actor Two",
  "genres": [1, 2, 3]
}
```

**Response:** `201 Created`

---

#### 4. Update Movie

```http
PUT /api/v1/movies/{movie_id}
```

**Request Body:** (all fields optional)

```json
{
  "title": "Updated Title",
  "release_year": 2024,
  "genres": [4, 5]
}
```

**Response:** `200 OK`

---

#### 5. Delete Movie

```http
DELETE /api/v1/movies/{movie_id}
```

**Response:** `204 No Content`

---

#### 6. Submit Rating

```http
POST /api/v1/movies/{movie_id}/ratings
```

**Request Body:**

```json
{
  "score": 8
}
```

**Validation:** Score must be between 1 and 10

**Example Response:**

```json
{
  "status": "success",
  "data": {
    "rating_id": 31001,
    "movie_id": 1,
    "score": 8,
    "created_at": "2025-12-31T04:39:29.954283+00:00"
  }
}
```

---

### Error Responses

All errors follow a consistent format:

```json
{
  "status": "failure",
  "error": {
    "code": 404,
    "message": "Movie not found"
  }
}
```

| Status Code | Description |
|-------------|-------------|
| `400` | Bad Request |
| `404` | Resource Not Found |
| `422` | Validation Error |
| `500` | Internal Server Error |

---

## 🚀 Getting Started

### Prerequisites

- **Docker** and **Docker Compose** (recommended)
- Or: Python 3.12+, PostgreSQL 16+, Poetry

---

### Option 1: Docker (Recommended)

#### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Movie-Rating-System.git
cd Movie-Rating-System
```

#### Step 2: Configure Environment

```bash
cp .env.example .env
```

#### Step 3: Start Services

```bash
docker compose up --build -d
```

#### Step 4: Run Migrations

```bash
docker compose exec app alembic upgrade head
```

#### Step 5: Seed Database (Optional but Recommended)

First, download the [TMDB](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) dataset files and place them in `scripts/`:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

Then run:

```bash
docker compose exec db psql -U movieuser -d moviedb -f /scripts/seeddb.sql
```

#### Step 6: Verify Seeding

```bash
docker compose exec app python scripts/seed_check.py
```

Expected output:

```
==================================================
Database Seeding Verification
==================================================
   Movies loaded:    1000
   Directors loaded: 2576
   Genres loaded:    20
   Ratings loaded:   ~20000
==================================================
✅ Seeding Successful!
```

#### Step 7: Access the API

- **API Base:** http://localhost:8000
- **Swagger UI:** http://localhost:8000/docs
- **Health Check:** http://localhost:8000/health

---

### Option 2: Local Development

#### Step 1: Install Poetry

```bash
pip install poetry
```

#### Step 2: Install Dependencies

```bash
poetry install
```

#### Step 3: Setup PostgreSQL

Create a database and update `.env`:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/moviedb
DEBUG=True
```

#### Step 4: Run Migrations

```bash
poetry run alembic upgrade head
```

#### Step 5: Start Server

```bash
poetry run uvicorn app.main:app --reload
```

---

## 🗄 Database

### Entity Relationship Diagram

```
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│  directors  │       │   movies    │       │   genres    │
├─────────────┤       ├─────────────┤       ├─────────────┤
│ id (PK)     │◄──────│ director_id │       │ id (PK)     │
│ name        │       │ id (PK)     │──────►│ name        │
│ birth_year  │       │ title       │       │ description │
│ description │       │ release_year│       └─────────────┘
└─────────────┘       │ cast        │              ▲
                      │ description │              │
                      └─────────────┘              │
                             │                     │
                             ▼                     │
                      ┌─────────────┐       ┌──────┴──────┐
                      │movie_ratings│       │movie_genres │
                      ├─────────────┤       ├─────────────┤
                      │ id (PK)     │       │ movie_id(FK)│
                      │ movie_id(FK)│       │ genre_id(FK)│
                      │ score       │       └─────────────┘
                      │ rated_at    │
                      └─────────────┘
```

### Tables Description

| Table | Description |
|-------|-------------|
| `directors` | Movie directors information |
| `genres` | Available movie genres (20 from TMDB) |
| `movies` | Main movie information |
| `movie_genres` | Many-to-many relationship between movies and genres |
| `movie_ratings` | User ratings for movies (1-10 scale) |

---

## 🧪 Testing

### Quick API Test with cURL

```bash
# List movies
curl http://localhost:8000/api/v1/movies

# Get movie details
curl http://localhost:8000/api/v1/movies/1

# Create movie
curl -X POST http://localhost:8000/api/v1/movies \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Movie", "director_id": 1, "genres": [1, 2]}'

# Submit rating
curl -X POST http://localhost:8000/api/v1/movies/1/ratings \
  -H "Content-Type: application/json" \
  -d '{"score": 8}'

# Delete movie
curl -X DELETE http://localhost:8000/api/v1/movies/1001
```

### Using Swagger UI

1. Navigate to http://localhost:8000/docs
2. Click on any endpoint
3. Click "Try it out"
4. Fill in parameters
5. Click "Execute"

---

## 📊 Logging

The application includes comprehensive logging for monitoring and debugging:

### Log Format

```
2025-12-31 04:16:35 - movie_rating - INFO - Fetching movies list (page=1, page_size=10, title=None, release_year=None, genre=None)
2025-12-31 04:16:35 - movie_rating - INFO - Returned 10 movies (total: 1000)
```

### Log Levels

| Level | Usage |
|-------|-------|
| `INFO` | Successful operations |
| `WARNING` | Non-critical issues (e.g., resource not found) |
| `ERROR` | Critical failures |

### Viewing Logs

```bash
# Real-time logs
docker compose logs -f app

# Last 100 lines
docker compose logs --tail=100 app
```

---

## 🛑 Stopping the Application

```bash
# Stop and remove containers
docker compose down

# Stop and remove containers with volumes (deletes database)
docker compose down -v
```

---

## 📄 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | - |
| `DEBUG` | Enable debug mode | `False` |

---

## 🤝 Team

| Name | Role | Responsibilities |
|------|------|-----------------|
| **Mehdi Gholami** | Backend Developer | APIs 1-4, 7 (GET, POST ratings), Logging, Docker |
| **Parsa Pourghasemi** | Backend Developer | APIs 5-6 (POST, PUT, DELETE movies) |

---

## 🎓 Course Information

- **Course:** Software Engineering
- **University:** Amirkabir University of Technology (AUT)
- **Semester:** Fall 2025

---

<div align="center">

**Made with ❤️ for Software Engineering Course**

</div>
