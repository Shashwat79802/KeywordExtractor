import logging
from fastapi.logger import logger


def get_gunicorn_logger():
    gunicorn_logger = logging.getLogger("gunicorn.error")
    logger.handlers = gunicorn_logger.handlers
    logger.setLevel(gunicorn_logger.level)
    return gunicorn_logger
