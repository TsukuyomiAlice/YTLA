# coding=utf-8
import os
import logging
import functools
from logging.handlers import RotatingFileHandler
from core.domain.area.frame.func import utilConfigs

# Logger configuration inherited from utilConfigs
LOG_LEVEL = utilConfigs.log_level_info  # Get log level from config
LOG_DIR = utilConfigs.log_folder_path  # Log directory path


def setup_logger(name, log_file, level=LOG_LEVEL, export_to_console=False):
    """
    Create and configure a logger instance with file rotation.

    Args:
        name (str): Logger name (recommended to use __name__)
        log_file (str): Log file name (.log suffix will be auto-added)
        level (int): Logging level (DEBUG/INFO/WARNING/ERROR/CRITICAL)
        export_to_console (bool): Enable console output if True

    Returns:
        logging.Logger: Configured logger instance with file handler

    Raises:
        OSError: If log directory creation fails
    """
    # Ensure log directory exists
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    # Full log path
    full_path = os.path.join(LOG_DIR, f"{log_file}.log")

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    # File handler with rotation (32MB per file)
    file_handler = RotatingFileHandler(
        full_path,
        maxBytes=32 * 1024 * 1024,
        backupCount=0,
        encoding='utf-8'
    )

    # Unified formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    if export_to_console:
        logger.addHandler(console_handler)

    return logger


def process_log(func):
    """
    Decorator for automatically logging process flow.

    Logs:
        - Function entry with parameters
        - Successful exit with result
        - Exceptions with traceback

    Args:
        func (callable): Function to be wrapped

    Returns:
        callable: Wrapped function with logging capability
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        process_info_logger.info(f" START   : {func.__name__}\nPARAMS  : {args} {kwargs}")
        try:
            result = func(*args, **kwargs)
            process_info_logger.info(f" FINISHED: {func.__name__}\nRESULT  : {result}\n")
            return result
        except Exception as e:
            process_error_logger.error(f" FAILED  : {func.__name__}\nCAUSE   : {str(e)}\n", exc_info=True)
            raise

    return wrapper


def router_log(func):
    """
    Decorator for automatically logging router flow.

    Logs:
        - Function entry with parameters
        - Successful exit with result
        - Exceptions with traceback

    Args:
        func (callable): Function to be wrapped

    Returns:
        callable: Wrapped function with logging capability
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        router_info_logger.info(f" START   : {func.__name__}\nPARAMS  : {args} {kwargs}")
        try:
            result = func(*args, **kwargs)
            router_info_logger.info(f" FINISHED: {func.__name__}\nRESULT  : {result}\n")
            return result
        except Exception as e:
            router_error_logger.error(f" FAILED  : {func.__name__}\nCAUSE   : {str(e)}\n", exc_info=True)
            raise

    return wrapper


db_info_logger = setup_logger("db_info", "db_msg_info", level=utilConfigs.log_level_info)
db_error_logger = setup_logger("db_error", "db_msg_error", level=utilConfigs.log_level_error)

process_info_logger = setup_logger("process_info", "process_msg_info", level=utilConfigs.log_level_info)
process_warning_logger = setup_logger("process_warning", "process_msg_warning", level=utilConfigs.log_level_warning)
process_error_logger = setup_logger("process_error", "process_msg_error", level=utilConfigs.log_level_error)

router_info_logger = setup_logger("router_info", "router_msg_info", level=utilConfigs.log_level_info)
router_error_logger = setup_logger("router_error", "router_msg_error", level=utilConfigs.log_level_error)
