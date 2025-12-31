"""Logging configuration for the application."""

import logging
import sys


def setup_logging(level: str = "INFO") -> logging.Logger:
    """
    Setup and configure logging for the application.

    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

    Returns:
        Configured logger instance
    """
    # Create logger
    app_logger = logging.getLogger("movie_rating")
    app_logger.setLevel(getattr(logging, level.upper(), logging.INFO))

    # Avoid duplicate handlers
    if app_logger.handlers:
        return app_logger

    # Create console handler
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)

    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    handler.setFormatter(formatter)

    # Add handler to logger
    app_logger.addHandler(handler)

    return app_logger


# Global logger instance
logger = setup_logging()