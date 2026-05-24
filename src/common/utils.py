import logging
import datetime
from pathlib import Path

logger: logging.Logger = logging.getLogger(f"{__name__}")


def ensure_dir(path: str) -> None:
    """确保文件路径存在

    Args:
        path (str): 待确认的文件路径
    """

    Path(path).mkdir(parents=False, exist_ok=True)


def read_text_file(path: str) -> str:
    """读取文本类文件内容

    Args:
        path (str): 文本路径

    Returns:
        str: 所读取内容
    """

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def get_current_timestamp() -> str:
    """生成当下时间戳

    Returns:
        str: 时间戳
    """

    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")


def generate_batch_id() -> str:
    """生成批次号

    Returns:
        str: 批次号
    """

    return datetime.datetime.now().strftime("BATCH_%Y%m%d%H%M%S")


def safe_divide(
    dividend: int | float, divisor: int | float, default: int = 0
) -> int | float:
    """安全除法, 避免除零错误

    Args:
        dividend (int | float): 被除数
        divisor (int | float): 除数
        default (int, optional): 除数为0时返回的默认值. Defaults to 0.

    Returns:
        int | float: 除法结果
    """

    try:
        return dividend / divisor
    except ZeroDivisionError:
        return default
