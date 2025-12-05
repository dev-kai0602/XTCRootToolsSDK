# <center> XTCRootToolsSDK开发规范  

---
#### <center> version 0.2.5

## 目录

1. [简介](#1-简介)
2. [代码布局规范](#2-代码布局规范)
3. [代码格式规范](#3-代码格式规范)
4. [命名规范](#4-命名规范)
5. [注释规范](#5-注释规范)
6. [类型注解规范](#6-类型注解规范)
7. [异常处理规范](#7-异常处理规范)
8. [导入规范](#8-导入规范)

---

## 1. 简介
本文描述了 Python 开发中的有关包、类、方法、实例变量、变量和常量的命名规范，用于规范 Python 编程过程中的命名和代码书写规范。

1. 程序代码作为重要的核心内容，有必要遵循统一的书写和编码规范；

2. 在程序设计总体方向上，有必要遵循统一的规范要求进行设计；

3. 遵循规范的要求，能够有效地减少编码过程中的错误；

4. 为了有效地提高程序的可维护性，编码方式需要遵循统一的规范。

---

## 2. 代码布局规范

* 缩进: Python严格使用缩进来体现代码之间的逻辑从属关系。一般使用4个空格作为一个缩进级别，不要使用制表符（Tab）。相同级别的代码块的缩进量必须相同。
* 行宽：每行代码最多不超过79个字符。如果需要换行，可以使用\。
* 空行：在函数之间、类之间和逻辑块之间添加一行空白行，以提高代码可读性。在运算符两侧、逗号后面等适当位置增加空格，使代码适当松散，不要过于密集。

---

## 3. 代码格式规范

### 1) 函数定义

* 定义函数时应指定参数类型和返回值类型，如:

> def add(number1: int, number2: int) -> int

而不是:

> def add(number1, number2):

### 2) 函数调用

* 调用函数传入参数时，各个个参数应用空格隔开, 且逗号应放在参数后面, 如:

> add(1, 2, 3)

而不是:

> add(1,2 ,3)

---

## 4. 命名规范

* 所有的变量和常量命名不应使用非ASCII编码的字符, 如: `watchModel = 'z11'`，而不是: `手表型号 = 'z11'`
* 所有的变量和常量命名不应使用缩写单词，如：`userName = 'root'`, 而不是：`uN = 'root'`
* 所有的变量和常量命名应该有意义，如: `userName = 'Peter'`, 而不是：`a = 'Peter'`

### 1) 变量
* 变量应遵循蛇形命名法，第一个单词的首字母小写，其余单词首字母大写，如: `user_name = 'Peter'`, 而不是：`userName = 'Peter'`

### 2) 常量
* 常量命名应只使用大写字母，每个单词之间使用下划线命名，如`MAX_NUMBER = 100`

### 4) 函数/类

* 所有的函数/类命名不应使用非ASCII编码的字符, 如: 

> def get_date(mode: int) -> str:

而不是: 

> def 获取数据(mode: int) -> str:

* 所有的函数/类命名不应使用缩写单词，如: 

> def get_date(mode: int) -> str:

而不是：

> def gd(mode: int) -> str:

* 所有的函数/类命名应该有意义，如: 

> def get_date(mode: int) -> str:

而不是：

> def a(mode: int) -> str:

### 5) 函数

* 函数应遵循蛇形命名法，单词之间用下划线分割，如:

> def print_date(mode: int) -> None: 

而不是: 

> def printDate(mode: int) -> None:

### 6) 类

* 类名应遵循大驼峰命名法，只使用大写字母，每个单词大写，如:

> class WatchRootTools:

而不是：

> class watch_root_tools:

### 7) 其他

#### 1) pytest

* pytest的函数应使用蛇形命名法， 并以`test_`开头, 如：

> def test_1() -> None:

---

## 5. 注释规范

* 单行注释：使用#符号进行单行注释。注释应简洁明了，解释代码的目的和实现方法。
* 多行注释：使用三个单引号'''或三个双引号"""将注释括起来，进行多行注释。
* 注释位置：注释应放在代码上方或旁边，以便读者能够轻松理解代码的含义。

### 1) 语句注释

* `for` 和 `while` 循环处最好写注释，说明其作用，如：

> \# 计算1+2+...+100的和  
> for num in range(1, 101): 

### 2) 函数注释

* 函数注释参考Google风格注释(如果没有参数/返回值等，则在该处填写'None')：

> """ 函数说明  
> **Args:**  
> $~~~~$ 参数名 (类型): 参数描述。包括默认值或特殊约束。  
> **Return:**  
> $~~~~$ 返回值类型: 返回值的描述。  
> **Raises:**  
> $~~~~$ 异常类型：异常触发条件。  
> """

如：

> def calculateArea(length: float, width: float) -> float:  
> """计算矩形的面积。  
> $~~~~$ Args:  
> $~~~~$ $~~~~$ length (float): 矩形的长度（单位：米）。  
> $~~~~$ $~~~~$ width (float): 矩形的宽度（单位：米）。  
> $~~~~$ Returns:    
> $~~~~$ $~~~~$ float: 矩形的面积（单位：平方米）。  
> $~~~~$ Raises:  
> $~~~~$ $~~~~$ ValueError: 如果长度或宽度为负数。  
> """  
> $~~~~$ if length < 0 or width < 0:  
> $~~~~$ $~~~~$ raise ValueError("长度和宽度必须为非负数。")  
> $~~~~$ return length * width  

### 3) 生成器函数注释

* 生成器函数注释参考Google风格注释

> """ 函数说明  
> **Args:**  
> $~~~~$ 参数名 (类型): 参数描述。包括默认值或特殊约束。  
> **Yields:**  
> $~~~~$ 返回值类型: 返回值的描述。  
> **Raises:**  
> $~~~~$ 异常类型：异常触发条件。  
> """

如: 

> def fibonacci(n: int) -> int:  
> """ 生成前 n 个斐波那契数。  
>
> Args:  
> $~~~~$ n (int): 要生成的斐波那契数数量。  
>
> Yields:  
> $~~~~$ int: 下一个斐波那契数。  
>
> Raises:  
> $~~~~$ ValueError: 如果 n 为负数。  
> """  
> $~~~~$ if n < 0:  
> $~~~~$ $~~~~$ raise ValueError("n 必须为非负数。")  
> $~~~~$ a, b = 0, 1  
> $~~~~$ for _ in range(n):  
> $~~~~$ $~~~~$ yield a  
> $~~~~$ a, b = b, a + b  

### 4) 类注释

* 类注释参考Google风格注释:

> """ 类说明   
> **Args:**  
> $~~~~$ 构造函数参数名 (类型): 描述  
> **Attributes:**  
> $~~~~$ 类的公共属性 (类型): 描述  
> **Raises:**  
> $~~~~$ 异常类型：异常触发条件。  
> """

如: 

> class DatabaseConnection:  
> $~~~~$ """管理数据库连接的类。  
>
> $~~~~$ Args:  
> $~~~~$ $~~~~$ host (str): 数据库主机地址。  
> $~~~~$ $~~~~$ port (int): 数据库端口号。  
> $~~~~$ $~~~~$ username (str): 用户名。  
> $~~~~$ $~~~~$ password (str): 密码。
>
> $~~~~$ Attributes:  
> $~~~~$ $~~~~$ connection (Connection): 活跃的数据库连接对象。
> $~~~~$ $~~~~$ is_connected (bool): 当前连接是否活跃。  
>
> $~~~~$ Raises:  
> $~~~~$ $~~~~$ConnectionError: 如果无法建立连接。  
> $~~~~$ """  
> $~~~~$ def __init__(self, host: str, port: int, username: str, password: str):  
> $~~~~$ $~~~~$ self.host = host  
> $~~~~$ $~~~~$ self.port = port  
> $~~~~$ $~~~~$ self.username = username  
> $~~~~$ $~~~~$ self.password = password  
> $~~~~$ $~~~~$ self.connection = None  
> $~~~~$ $~~~~$ self.is_connected = False 

### 5) 模块注释

* 模块注释参考Google风格注释:

> """ 模块说明  
> 
> 模块的详细描述  
>
> """

如:

> """ 日志模块  
>
> 该模块用于记录日志，格式为: [类型] 年:月:日 时:分:秒
>
> """

### 6) 自定义数据结构注释

#### (1) 枚举类

* 定义枚举类时应写下这个枚举类的作用:

> """ 枚举类作用 """

如：

> class LoggingLevel(enum.Enum):
> """ 这个枚举类用于枚举日志的各个等级 """

---

## 6. 类型注解规范

* **基本类型注解**：所有函数参数和返回值尽量写类型注解
* **复杂类型**：使用`typing`模块处理复杂类型
如：

> from typing import List, Dict, Optional, Union
>
> def processDevices(  
> $~~~~$ devices: List[str],   
> $~~~~$ config: Optional[Dict[str, Union[int, str]]] = None) -> bool:  
> """处理设备列表"""  
> $~~~~$ pass  


## 7. 异常处理规范

* **自定义异常**：创建项目特定的异常类
* **异常链**：使用`raise NewException from original_error`保留原始异常
* **具体异常**：避免裸`except:`语句
如：

> try:  
> $~~~~$ device.connect()  
> except DeviceNotFoundError:
> $~~~~$ # 处理特定异常  
> $~~~~$ logger.error("设备未找到")  
> except Exception as e:  
> $~~~~$ # 记录并重新抛出  
> $~~~~$ logger.error(f"连接失败: {e}")  
> $~~~~$ raise ConnectionError("设备连接失败") from e  

---

## 8. 导入规范

* **分组导入**：按标准库、第三方库、本地库分组
* **绝对导入**：使用绝对导入而非相对导入
* **避免通配符**：禁止使用`from module import *`
如：

> \# 标准库  
> import os  
> import sys  
> from typing import Dict, List  
>
> \# 第三方库  
> import requests  
> from loguru import logger  
>  
> \# 本地模块  
> from xtcroot.device.manager import DeviceManager  
> from .exceptions import RootError  

---

### 该文档创建时间: 2025/10/17  
### 最后修改时间: 2025/11/2
