"""日志模块

    用于记录日志，格式为: 模块名字: [类型] 年:月:日 时:分:秒 内容 , 可以用该模块的 makeLogging 函数实现，该函数需要log_path(日志文件夹
地址) 和 module_name(模块名字) 这两个参数，该函数返回值为 logging.Logger 实例

使用示例：
    loger = init_logging('log.log', '示例模块名', level=logging.INFO)
    #                    地址        名字         日志最低等级
    loger.info('这是一则INFO信息')

"""

import logging
import pathlib
import time
import typing

def init_logging(log_path: pathlib.Path,
                 module_name: str,
                 level: typing.Literal[
                     logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL
                 ] = logging.DEBUG
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
        FileNotFoundError: 日志文件夹不存在
        IsADirectoryError: 路径是目录而不是文件
    """
    # 检查文件夹是否存在及是不是文件夹
    if not log_path.exists():
        raise FileNotFoundError('该目录不存在')
    elif log_path.is_file():
        raise IsADirectoryError(f'该地址({log_path.resolve()})为文件,并非文件夹')

    # 创建logger实例
    logger = logging.getLogger(module_name)
    logger.setLevel(level)

    # 创建handler
    file_handler = logging.FileHandler(log_path / f"{module_name + time.strftime(" %Y-%m-%d", time.localtime())}.log", encoding="utf-8")
    file_handler.setLevel(level)

    # 输出到日志的格式
    handler_formatter = logging.Formatter(f"{module_name}: [%(levelname)s] %(asctime)s %(message)s")
    file_handler.setFormatter(handler_formatter)

    # 添加handler
    logger.addHandler(file_handler)

    return logger
