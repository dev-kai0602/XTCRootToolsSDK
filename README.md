# 因为本人手表被老登笑纳了(期末才能拿回)，无测试用机，项目被迫暂停

# <center> XTCRootToolsSDK

---

### <center> XTCRoot工具SDK

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> ⚠️ **重要免责声明**
>
> - 本工具仅用于**技术研究和学习目的**，严禁用于任何非法用途
> - 对设备进行Root操作可能导致：**设备变砖、失去官方保修、系统不稳定**等风险
> - 使用者需自行承担因使用本工具而产生的**一切后果和法律责任**
> - 继续使用本工具即表示您已阅读并同意以上条款

#### 完整免责声明请见[DISCLAIMER.md](DISCLAIMER.md)

---

## 简介

* 该项目把小天才电话手表获取Root权限及安装第三方应用的代码集成在一起（后期将会添加其他功能）(目前还在开发中）

---

## 目录

1) [简介](#简介)
2) [SDK环境要求](#sdk环境要求)
3) [文件目录介绍](#文件目录介绍)
4) [备注](#备注)

---

## SDK环境要求

* python解释器版本 >= 3.13.8
* uv版本 >= 0.9.5

---

## 文件目录介绍

```text
XTCRootTools/  
├── 📁 XTCRoot/                          # 主包目录（核心代码）  
│   ├── 📄 __init__.py                   # 包初始化文件  
│   ├── 📄 core.py                       # 核心类（RootManager, DeviceManager等）  
│   ├── 📄 exceptions.py                 # 自定义异常  
│   │   
│   ├── 📁 device/                       # 设备相关模块  
│   │   ├── __init__.py  
│   │   └── manager.py                   # 设备管理器  
│   │   
│   ├── 📁 modules/    
│   │   ├── __init__.py    
│   │   └── Logging.py  # 日志模块
│   │   
│   ├── 📁 root/                         # Root流程模块  
│   │   ├── __init__.py  
│   │   ├── executor.py                  # Root执行器  
│   │   └── methods/                     # 不同Root方法  
│   │       └── __init__.py  
│   │   
│   └── 📁 utils/                        # 工具函数  
│       └── __init__.py  
│   
├── 📁 resources/                        # 资源文件（与代码分离）  
│   │ 
│   ├── 📁 drivers/                      # 驱动文件  
│   │   
│   ├── 📁 tools/                        # 必要工具  
│   │   
│   └── 📁 config/                       # 配置文件  
│       └── config.json  
│   
├── 📁 scripts/                          # 辅助脚本 
│   
├── 📁 tests/                            # 测试代码  
│   └── 📄 test_logging.py    
│   
├── 📁 docs/                             # 文档    
│   ├── 📄 SDK.md    
│   └── 📄 XTCRootToolsSDK开发规范.md   
│   
├── 📄 pyproject.toml                    # 项目配置  
├── 📄 README.md                         # 项目说明  
├── 📄 uv.lock                           # UV环境管理
├── 📄 .python-version                   # python环境版本
├── 📄 pytest.ini                        # pytest配置文件
├── 📄 DISCLAIMER.md                     # 免责声明
├── 📄 LICENSE                           # 开源协议
└── 📄 .gitignore                        # Git忽略规则  
```

---

## 备注

1) 如果有好的想法或建议，请提 Issues
