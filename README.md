# <center> XTCRootToolsSDK

---

### <center> XTCRoot工具SDK

## 简介

* 该项目把小天才电话手表获取Root权限及安装第三方应用的代码集成在一起（后期将会添加其他功能），该项目仅用于学习小天才电话手表Root及安装第三方应用原理，不得用于商业用途(目前还在开发中）

---

## 目录

1) [简介](#简介)
2) [SDK环境要求](#sdk环境要求)
3) [文件目录介绍](#文件目录介绍)
4) [备注](#备注)
5) [免责声明](#免责声明)

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
│   │   ├── manager.py                   # 设备管理器  
│   │   └── detectors.py                 # 设备检测  
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
├── 📁 log/                              # 日志文件  
│   
├── 📄 pyproject.toml                    # 项目配置  
├── 📄 README.md                         # 项目说明  
├── 📄 uv.lock                           # UV环境管理
├── 📄 .python-version                   # python环境版本
├── 📄 pytest.ini                        # pytest配置文件
└── 📄 .gitignore                        # Git忽略规则  
```

---

## 备注

1) 如果有好的想法或建议，请提 Issues

## 免责声明

本工具仅用于技术研究和学习目的。使用者需自行承担因使用本工具而产生的所有风险和责任。

继续使用即表示您已阅读并同意：
- 可能违反设备制造商的保修条款
- 可能导致设备损坏或数据丢失
- 使用者承担所有法律责任和后果
