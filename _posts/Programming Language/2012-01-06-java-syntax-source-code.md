---
layout: post
title: Java语法之源代码组织
categories:
- Programming Language
tags:
- Java
---

## 源文件
- 每个java源文件中最多只能有一个public类，也可以没有(不推荐)
- 如果java源文件中包含一个public类，则文件名必须与public类名相同

## 包结构
- 为解决名字冲突问题，同时将类按照包组织起来
- 如果没有定义包，则使用默认包；
- 语法：package top.second.father;
	- 必须时文件中除注释以外的第一个程序代码；
	- 包路径对应着源代码的文件路径
	- 包路径一般使用域名的倒叙，便于创建独一无二的包名
- 引入包：
	- 引入指定类：import top.second.father.sun;
	- 引入指定包中所有public类：import top.second.father.*;
	- 静态引入：import static top.second.father.*;
		- 可直接使用指定包中所有静态方法而不用指定类名
- 如果引入的多个包中包含冲突的名字，则如果不使用就不会导致冲突
	- 原理：使用时才会加载指定的类；
	- 避免，通过加完整的包路径就可避免冲突；

## jre程序包
- java程序发布方式
	- 运行jre程序
- 打包成jre程序