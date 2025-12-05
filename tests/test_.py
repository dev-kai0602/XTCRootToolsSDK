""" 测试文件 """
import pathlib

def test_():
    f = pathlib.Path("../logs")
    flg = (not f.exists() or not f.is_file())
    print(flg)