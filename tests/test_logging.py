""" 测试文件，用于测试modules.logging.py文件 """
import logging
import pathlib

import pytest

from XTCRoot import modules

def test_logging() -> None:
    """ 测试函数1 """
    logPath = pathlib.Path("../logs")
    moduleName = "testModule"

    for level in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]:
        testCase = modules.Logging.init_logging(logPath, moduleName, level)
        testCase.debug("test text - debug")
        testCase.info("test text - info")
        testCase.warning("test text - warning")
        testCase.error("test text - error")
        testCase.critical("test text - critical")

if __name__ == '__main__':
    pytest.main()
