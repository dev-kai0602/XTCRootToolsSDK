""" 测试文件，用于测试modules.logging.py文件 """
import logging
import pathlib

import pytest

from XTCRoot import utils

def test_logging() -> None:
    """ 测试函数1 """

    # 如需在其他
    log_path = pathlib.Path("/media/kai/data/OpenSourceProject/XTCRootToolsSDK/logs")
    module_name = "testModule"

    for level in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]:
        test_case = utils.Logging.init_logging(log_path, module_name, level)
        test_case.debug("test text - debug")
        test_case.info("test text - info")
        test_case.warning("test text - warning")
        test_case.error("test text - error")
        test_case.critical("test text - critical")

if __name__ == '__main__':
    pytest.main()
