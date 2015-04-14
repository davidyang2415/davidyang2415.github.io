---
layout:post
title:Java Exception
categries:
- Programming Language
tags:
- Java
---

# Java语法之异常处理
--------------------------------------
## 错误处理概念
- 异常与错误

## 抛出异常
- 关键字：throw
- 抛出异常对象

## 捕获异常
- 捕获异常：try{}catch(){}finally{}
	- finally，无论是否产生异常都必须执行的内容
	- catch捕获的异常的顺序必须是逐渐扩展的
- 异常类体系：
	- 合理设置异常捕获顺序
	- 通过异常基类捕获所有异常

## 异常声明
- 声明方法可能抛出的异常
- 继承体系中，重写方法的异常声明的范围

## 重新抛出异常
- 异常抛出链

## 异常类体系
### 标准异常类系统 
- Throwable
- Error
- Exception

### 自定义异常类