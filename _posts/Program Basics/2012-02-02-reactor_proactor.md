---
layout: post
title: 设计模式之Reactor与Proactor
categories:
- Basic Programming
tags:
- basic programming
- design pattern
---

# 设计模式之Reactor模式与Proactor模式
------------------
- 小明买书的例子：
	- 小明去买书，如果没有书则会等待，直到有书或书店关门(超时)
	- 小明告诉销售员，书到货后通知小明，小明在收到通知后去书店取书
	- 小明告诉销售员，书到货后送到小明家，书送到小明家后通知小明一声
- 在以上例子中第二种情况描述的是Reactor模式，第三种描述的是Proactor模式
- 使用Reactor的例子是Linux的epoll通信模型
- 使用Proactor的例子是Windows的IOCP通信模型