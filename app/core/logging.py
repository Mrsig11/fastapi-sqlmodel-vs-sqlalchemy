import logging
import sys


def setup_logging(level: str = "INFO"):
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    # Nettoyage des handlers existants (uvicorn, reload, etc.)
    if root_logger.handlers:
        root_logger.handlers.clear()

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    console_handler.setFormatter(formatter)

    root_logger.addHandler(console_handler)

    # Réglage des loggers uvicorn
    logging.getLogger("uvicorn").setLevel(level)
    logging.getLogger("uvicorn.error").setLevel(level)
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
