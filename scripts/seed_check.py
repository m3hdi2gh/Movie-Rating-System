import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://movieuser:moviepass123@localhost:5432/moviedb"
)

engine = create_engine(DATABASE_URL)


def verify_seeding():
    """Checks if the database has the expected number of records after seeding."""
    try:
        with Session(engine) as session:
            movie_count = session.execute(
                text("SELECT COUNT(*) FROM movies")
            ).scalar_one()

            director_count = session.execute(
                text("SELECT COUNT(*) FROM directors")
            ).scalar_one()

            genre_count = session.execute(
                text("SELECT COUNT(*) FROM genres")
            ).scalar_one()

            rating_count = session.execute(
                text("SELECT COUNT(*) FROM movie_ratings")
            ).scalar_one()

            print("=" * 50)
            print("Database Seeding Verification")
            print("=" * 50)
            print(f"   Movies loaded:    {movie_count}")
            print(f"   Directors loaded: {director_count}")
            print(f"   Genres loaded:    {genre_count}")
            print(f"   Ratings loaded:   {rating_count}")
            print("=" * 50)

            if movie_count == 1000 and director_count > 1000:
                print("✅ Seeding Successful!")
                return True
            else:
                print(f"❌ Seeding Failed. Expected 1000 movies, found {movie_count}.")
                return False

    except Exception as e:
        print(f"❌ Database connection or query failed: {e}")
        return False


if __name__ == "__main__":
    verify_seeding()