"""Base exception classes for the application."""


class AppException(Exception):
    """Base exception for all application exceptions."""

    def __init__(self, message: str, code: int = 500):
        self.message = message
        self.code = code
        super().__init__(self.message)