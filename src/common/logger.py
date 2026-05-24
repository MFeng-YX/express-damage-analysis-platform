import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logging():

    # 创建根日志器
    root_logger: logging.Logger = logging.getLogger()
    # 避免重复初始化控制台
    if root_logger.handlers:
        return

    root_logger.setLevel(logging.INFO)

    # 获取文件路径
    BASE_PATH: Path = Path(__file__).resolve().parents[2]
    LOG_DIR: Path = BASE_PATH / "log"
    LOG_DIR.mkdir(parents=False, exist_ok=True)
    log_file: Path = LOG_DIR / "log.log"

    # 创建文件日志器
    file_handle: RotatingFileHandler = RotatingFileHandler(
        log_file, mode="a", maxBytes=1024 * 1024, backupCount=5, encoding="utf-8"
    )
    file_formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handle.setLevel(logging.INFO)
    file_handle.setFormatter(file_formatter)

    # 创建控制台日志
    console_handle: logging.Handler = logging.StreamHandler()
    console_formatter = logging.Formatter(
        fmt="%(asctime)s | %(name)s | %(message)s", datefmt="%H:%M:%S"
    )
    console_handle.setLevel(logging.INFO)
    console_handle.setFormatter(console_formatter)

    # 添加 handler 到 logger
    root_logger.addHandler(file_handle)
    root_logger.addHandler(console_handle)
