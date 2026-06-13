import os
import sqlalchemy as sa

from contextlib import contextmanager
from sqlalchemy import Engine

_engine: Engine | None = None


def get_engine() -> Engine:
    """获取数据库引擎 Engine

    Returns:
        Engine : 数据库引擎
    """
    global _engine

    if not _engine:
        db_url = os.getenv("DB_URL")

        if not db_url:
            raise RuntimeError("环境变量 DB_URL未配置, 请配置.")

        _engine = sa.create_engine(db_url, echo=True, pool_size=20)

    return _engine


@contextmanager
def get_connection():
    """数据库连接

    Yields:
        _type_: 自动管理数据库连接
    """
    engine: Engine = get_engine()

    with engine.connect() as connection:
        yield connection
