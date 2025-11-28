"""日志模块

    用于记录日志，格式为: 模块名字: [类型] 年:月:日 时:分:秒 内容 , 可以用该模块的 makeLogging 函数实现，该函数需要log_path(日志文件夹
地址) 和 module_name(模块名字) 这两个参数，该函数返回值为 logging.Logger 实例

"""

import logging
import pathlib
import time
import typing

def init_logging(log_path: pathlib.Path,
                 module_name: str,
                 level: typing.Literal[10, 20, 30 ,40, 50] = 10
                 ) -> logging.Logger:
    """创建日志函数，创建logger实例，并初始化

    Args:
        log_path (str): 存放日志文件的文件夹地址
        module_name (str): 模块名
        level: typing.Literal[10 (logging.DEBUG), 20 (logging.INFO), 30 (logging.WARNING),
                 40 (logging.ERROR), 50 (logging.CRITICAL)] = 10 (logging.DEBUG): 用于指定输出的最小等级

    Returns:
        logging.Logger: logger实例

    Raises:
        FileNotFoundError: 当指定的日志文件夹不存在时，抛出该异常
    """
    # 检查文件夹是否存在
    if not (log_path.exists() and log_path.is_dir()):
        raise FileNotFoundError

    # 创建logger实例
    logger = logging.getLogger(module_name)
    logger.setLevel(level)

    # 创建handler
    file_handler = logging.FileHandler(log_path / f"{module_name + time.strftime(" %Y-%m-%d", time.localtime())}.log", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)

    # 输出到日志的格式
    handler_formatter = logging.Formatter(f"{module_name}: [%(levelname)s] %(asctime)s %(message)s")
    file_handler.setFormatter(handler_formatter)

    # 添加handler
    logger.addHandler(file_handler)

    return logger
