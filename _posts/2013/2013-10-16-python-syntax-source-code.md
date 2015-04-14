---
layout:post
title:Python Source Code
categries:
- Programming Language
tags:
- Python
---

# Python语法之源代码组织
------------------
## 源代码文件
- 源码文件后缀：
	- .py，源文件
	- .pyc(bytecode,二进制编码) 
	- .pyo(bytecode optimized，优化后的二进制编码)
	- .pyd(binary module,动态库文件)
	
## 模块(module)
- 模块是包含了所有定义的函数和变量的可重用的.py文件
- 模块初始化的过程仅在第一次import模块的时候进行。
- 一般来说，一个module对应一个.py文件
- 一个模块只被加载一次，无论被导入多少次
- module查找顺序：
	- 当前目录 -> 环境变量PYTHONPATH -> python安装目录
	- 避免跟库同名module，可通过包组织来避免
- 引入模块：
	- import module [as alias][,...]
	- from module import name [as alias][,...]
	- from module import *
	- reload(module)
- 模块常用变量:
	- __name__ ->str
	- __file__ ->str
- 常用模块：
	- __builtins__模块

## 包(package)
- 一般来说，一个package对应是一个文件夹，包含一个__init__.py文件
- package中可包含package和modules
- 使用时采用package.package.module.attr形式

## 命名空间
- 命令空间，是标识符能被找到的位置
- 命令空间：__builtins__(系统自动加载)、Global namespace、Local namespace
- 命令空间查找顺序：当前命令空间 -> Global namespace -> __builtins__ 
- 相关函数：
	- del 从命名空间中删除已经存在标识符
	- globals() -> dict
	- locals() -> dict
	- dir([object]) -> list
	- vars([object]) -> dict
- 其他命令空间：Class namespace,Object namesacpe
- 命名空间可以嵌套，但内层命令空间标识符会隐藏外层同名标识符
- 在Local namespace中使用Global namespace标识符，使用global关键字声明