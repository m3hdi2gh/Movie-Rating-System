"""HTTP-specific exception classes."""

from app.exceptions.base import AppException


class NotFoundException(AppException):
    """Raised when a resource is not found."""

    def __init__(self, message: str = "Resource not found"):
        super().__init__(message=message, code=404)


class ValidationException(AppException):
    """Raised when validation fails."""

    def __init__(self, message: str = "Validation error"):
        super().__init__(message=message, code=422)


class BadRequestException(AppException):
    """Raised when request is malformed."""

    def __init__(self, message: str = "Bad request"):
        super().__init__(message=message, code=400)


class ConflictException(AppException):
    """Raised when there's a conflict (e.g., duplicate entry)."""

    def __init__(self, message: str = "Conflict"):
        super().__init__(message=message, code=409)