"""Movie controller - API endpoints for movies and ratings."""

from typing import Optional
from fastapi import APIRouter, Depends, Query, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services import MovieService, RatingService
from app.schemas import RatingCreate
from app.exceptions import ValidationException

router = APIRouter()


# =============================================================================
# API 1 & 2: GET /movies - List movies with pagination and filtering
# =============================================================================

@router.get("/movies")
def get_movies(
        page: int = Query(1, ge=1, description="Page number"),
        page_size: int = Query(10, ge=1, le=100, description="Items per page"),
        title: Optional[str] = Query(None, description="Filter by title (partial match)"),
        release_year: Optional[int] = Query(None, ge=1800, le=2100, description="Filter by release year"),
        genre: Optional[str] = Query(None, description="Filter by genre name"),
        db: Session = Depends(get_db),
):
    """
    Get list of movies with pagination and optional filters.

    - **page**: Page number (default: 1)
    - **page_size**: Items per page (default: 10, max: 100)
    - **title**: Filter by title (partial match, case-insensitive)
    - **release_year**: Filter by exact release year
    - **genre**: Filter by genre name (partial match, case-insensitive)
    """
    service = MovieService(db)
    movies, total_count = service.get_movies(
        page=page,
        page_size=page_size,
        title=title,
        release_year=release_year,
        genre=genre,
    )

    return {
        "status": "success",
        "data": {
            "page": page,
            "page_size": page_size,
            "total_items": total_count,
            "items": movies,
        }
    }


# =============================================================================
# API 3: GET /movies/{movie_id} - Get movie details
# =============================================================================

@router.get("/movies/{movie_id}")
def get_movie(
        movie_id: int,
        db: Session = Depends(get_db),
):
    """
    Get detailed information about a specific movie.

    - **movie_id**: The ID of the movie to retrieve
    """
    service = MovieService(db)
    movie = service.get_movie_by_id(movie_id)

    return {
        "status": "success",
        "data": movie,
    }


# =============================================================================
# API 7: POST /movies/{movie_id}/ratings - Create rating for a movie
# =============================================================================

@router.post("/movies/{movie_id}/ratings", status_code=status.HTTP_201_CREATED)
def create_rating(
        movie_id: int,
        rating_data: RatingCreate,
        db: Session = Depends(get_db),
):
    """
    Submit a rating for a movie.

    - **movie_id**: The ID of the movie to rate
    - **score**: Rating score between 1 and 10
    """
    service = RatingService(db)
    rating = service.create_rating(movie_id=movie_id, score=rating_data.score)

    return {
        "status": "success",
        "data": rating,
    }

# =============================================================================
# APIs 4, 5, 6: POST, PUT, DELETE /movies (To be implement by parsa)
# =============================================================================

# @router.post("/movies", status_code=status.HTTP_201_CREATED)
# def create_movie(...):
#     pass

# @router.put("/movies/{movie_id}")
# def update_movie(...):
#     pass

# @router.delete("/movies/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_movie(...):
#     pass