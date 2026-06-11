class AppError(Exception):
    """项目基础异常类

    Args:
        Exception (_type_): 异常类
    """

    def __init__(self, message: str, code: str | None = None) -> None:
        """初始化 AppError 类

        Args:
            message (str): 错误异常信息
            code (str | None, optional): 异常编码. Defaults to None.
        """

        self.message = message
        self.code = code
        super().__init__(message)

    def __str__(self) -> str:
        """打印内容

        Returns:
            str: 输出打印信息
        """
        if self.code:
            return f"[{self.code}]: {self.message}"
        return self.message


class ConfigError(AppError):
    """配置错误

    Args:
        AppError (_type_): 项目异常基础类
    """

    pass


class DatabaseError(AppError):
    """数据库连接错误

    Args:
        AppError (_type_): 项目异常基础类
    """

    pass


class ExcelReadError(AppError):
    """Excel文件读取错误

    Args:
        AppError (_type_): 项目异常基类
    """

    pass


class FieldMappingError(AppError):
    """字段映射错误

    Args:
        AppError (_type_): 项目异常基类
    """

    pass


class ValidationError(AppError):
    """数据验证错误

    Args:
        AppError (_type_): 项目异常基类
    """

    pass


class ETLError(AppError):
    """数据ETL流程错误

    Args:
        AppError (_type_): 项目异常基类
    """

    pass


class APIServiceError(AppError):
    """API服务错误

    Args:
        AppError (_type_): 项目异常基类
    """

    pass
