"""异常模块

    该模块包含了XTCRootToolsSDK运行时可能会发生的异常

"""

class DevicesError:
    """ ADB设备错误类 """

    class DeviceNotFoundError(Exception):
        """ 未找到设备

            Args:
                host (str) = '': 地址
                port (int) = -1: 端口号
                message (str) = '': 报错信息
        """

        def __init__(self, host: str = '', port: int = 0, message: str = ''):
            message_list: list = []

            if host:
                message_list.append(f"host: {host}")
            if port:
                message_list.append(f"port: {port}")
            if message:
                message_list.append(message)

            super().__init__(" ".join(message_list))

    class DeviceNotConnect(Exception):
        """ 设备断开连接

            Args:
                *args: 报错信息

        """

        def __init__(self, *args):
            super().__init__(args)
