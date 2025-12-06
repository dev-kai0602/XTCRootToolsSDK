""" XTC手表管理器

    该模块用于管理连接的XTC手表
"""

import typing

import ppadb.client

# from .. import exceptions
import exceptions

class Manager:
    """ XTC设管理类，用于管理连接到电脑的XTC设备

    Args:
        adb_setting (dict): ADB配置文件内容

    Raises:
        exceptions.DevicesError.DeviceNotFoundError: 未找到设备

    """ # TODO: 使用手表测试代码

    def __init__(self, adb_setting: dict) -> None:
        # 初始化
        self.adb_setting: dict = adb_setting

        self.client = ppadb.client.Client(host=self.adb_setting['host'], port=self.adb_setting['port']) # 连接ADB服务
        self.devices = self.client.devices() # 获取并选择设备
        if not self.devices: # 没有找到设备时报错
            raise exceptions.DevicesError.DeviceNotFoundError(
                self.adb_setting['host'], self.adb_setting['port'], '未找到设备')

        self.device = self.devices[0] # 默认选择第一个设备

        self.device_information: dict = { # 设备信息
            'inner_model': self.device.shell('adb shell getprop ro.product.innermodel').replace('\n', '').replace('\r', ''),
            'public_model': self.device.shell('adb shell getprop ro.product.model').replace('\n', '').replace('\r', ''),
            'android_version': self.device.shell('getprop ro.build.version.release').replace('\n', '').replace('\r', ''),
            'android_SDK_version': self.device.shell('adb shell getprop ro.build.version.sdk').replace('\n', '').replace('\r', ''),
            'system_version': self.device.shell('shell getprop ro.product.current.softversion').replace('\n', '').replace('\n', ''),
            'is_v3': self.device.shell('adb shell getprop persist.sys.isv3').replace('\n', '').replace('\n', ''),
        }

    def is_connect(self) -> None:
        """ 检查设备是否还在连接

        Returns:
            None

        Raises:
            exceptions.DevicesError.DeviceNotConnect: 设备未连接

        """

        try:
            self.device.get_serial_no()

        except RuntimeError:
            raise exceptions.DevicesError.DeviceNotConnect

    def shell(self, *command) -> str:
        """ 设备shell命令执行器，可以发送指令到手表并执行

        Args:
            *command: 指令

        Returns:
            str: 执行命令后手表标准输出流输出的内容

        Raises:
            exceptions.DevicesError.DeviceNotConnect: 设备断开

        """

        self.is_connect()
        stdout = self.device.shell(command)

        return stdout

    def reboot(self, mode: typing.Literal['edl', 'fastboot', ''] = '') -> None:
        """ 重启设备

        Args:
            mode(typing.Literal['edl', 'fastboot', ''] = ''): 重启后进入的模式(edl(9008), fastboot)

        Returns:
            None

        Raises:
            exceptions.DevicesError.DeviceNotConnect: 设备断开

        """
        self.is_connect()
        self.shell(f"reboot {mode}")


if __name__ == '__main__':
    # TODO: 上传到GitHub前得把这段代码删除
    import json, os

    with open('/resources/config/ADB_setting.json', encoding='utf-8') as f:
        a = Manager(json.loads(f.read()))

    for a, b in a.device_information.items():
        print(f"{a}: {b}")
