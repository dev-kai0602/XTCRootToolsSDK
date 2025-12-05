""" XTC手表管理器

    该模块用于管理连接的XTC手表
"""

import ppadb.client

from .. import exceptions

class Manager:
    """ XTC设管理类，用于管理连接到电脑的XTC设备

    Args:
        adb_setting (dict): ADB配置文件内容

    Raises:
        exceptions.DevicesError.DeviceNotFoundError: 未找到设备

    """

    def __init__(self, adb_setting: dict) -> None:
        # 初始化
        self.adb_setting: dict = adb_setting

        self.client = ppadb.client.Client(host=self.adb_setting['host'], port=self.adb_setting['port']) # 连接ADB服务
        self.devices = self.client.devices() # 获取并选择设备
        if not self.devices: # 没有找到设备时报错
            raise exceptions.DevicesError.DeviceNotFoundError(
                self.adb_setting['host'], self.adb_setting['port'], '未找到设备')

        self.device = self.devices[0] # 默认选择第一个设备

    def get_device_information(self) -> dict:
        """ XTC设备信息获取函数

        Returns:
            dict: 设备信息
        """
