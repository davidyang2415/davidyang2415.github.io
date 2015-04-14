---
layout:post
title:Python Basic Language
categries:
- Programming Language
tags:
- Python
---

# Python语法之语言基础
------------------
## 核心概念：一切都是对象
- 这里说的一切包括：函数、类、类实例、模块、复数和文件。
- 对象具有特性：
	- 赋值：将变量绑定到对象上

## 语言特征
- 语言类型：
	- 动态语言、面向对象语言
	- 格式化语言，使用缩进划分语句块
- 版本信息：
	- 2.x(更好的第三方模块支持)与3.x的区别：不兼容
	- 解释器实现版本：Cython(C语言实现-默认版本),Jython(Java实现)等
		
## 语言规范
### 源文件
- .py文件是python源代码文件
- 通过预编译提高运行速度，常用后缀：.pyc等
### 源代码格式
- 文件头格式：
	- #!/usr/bin/env python 可选，指出脚本执行解释器位置
	- #coding:utf-8 可选，指出源文件编码格式
- 注释
	- 单行注释：以#符号开头
	- 多行注释：使用三引号字符串作为多行注释
	- 文档注释：模块、函数及类的注释
		- 使用三引号字符串，位置必须是函数、类等的第一部分
- 常用输入与输出：
	- 输出：print
	- 输入：input(str),raw_input(str)--所有输入作为原始数据即字符串
- 技巧：
	- 模块属性__name__可判断是import还是直接执行，用于单元测试
		- if __name__=='__main__':
### 编码规范
- 命名规范

## 开发环境
- 环境变量：PYTHONPATH
- 开发工具：
	- 常用开发IDE：idle，pycharm，eclipse + pydev
	- 发布python包
	- 打包成平台可执行文件：Pyinstaller