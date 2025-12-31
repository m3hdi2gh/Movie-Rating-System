"""Base schemas for API responses."""

from typing import TypeVar, Generic, List
from pydantic import BaseModel

T = TypeVar("T")


class ErrorDetail(BaseModel):
    """Error detail schema."""

    code: int
    message: str


class ErrorResponse(BaseModel):
    """Standard error response."""

    status: str = "failure"
    error: ErrorDetail


class SuccessResponse(BaseModel, Generic[T]):
    """Standard success response."""

    status: str = "success"
    data: T


class PaginatedData(BaseModel, Generic[T]):
    """Paginated data structure."""

    page: int
    page_size: int
    total_items: int
    items: List[T]


class PaginatedResponse(BaseModel, Generic[T]):
    """Standard paginated response."""

    status: str = "success"
    data: PaginatedData[T]