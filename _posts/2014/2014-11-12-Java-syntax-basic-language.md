---
layout:post
title:Java Basic Language
categries:
- Programming Language
tags:
- Java
---

# Java语法之语言基础
--------------------------------------
## 语言特性
- 语言类型
	- 强类型语言：必须先声明类型再使用
	- 静态类型语言：先编译再运行
	- 面向对象语言
- 跨平台与性能：
	- 通过Java Virtual Machine(Java虚拟机)支持跨平台，即在java程序和操作系统间做一层适配
	- 为了支持跨平台特性而牺牲了一定的性能
	- 在硬件性能持续提升的背景下，性能不在是瓶颈
- 应用领域
	- web领域开发
	- 服务器开发
	- GUI程序
	
## 程序开发
- 运行环境
	- Java虚拟机(JVM)：分为运行环境(jre)与开发工具(jdk,包含jre)
	- 环境变量的设置
- 开发工具
	- 编译程序javac，运行程序java
	- 常用ide:eclipse,IntelliJ IDEA
	- 程序管理：ant,maven
	
## 语言规范
- 注释
	- // 单行注释
	- /\* 多行注释 \*/
	- /\*\* 文档注释 \*/
		- 可通过javadoc工具提取成文档
		- 可使用文档标签，如@version,@author,@param,@return,throws等
- 编码风格
	- 类名：多单词拼接，每个单词的首字母都大写，包括首字母
	- 常量：多单词用下划线拼接，每个单词都大写
	- 其他：多单词拼接，除首个单词外其他单词首字母都大写