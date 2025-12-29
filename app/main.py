from fastapi import FastAPI

app = FastAPI(
    title="Movie Rating System",
    description="Backend API for managing movies and ratings",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "Welcome to Movie Rating System API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}