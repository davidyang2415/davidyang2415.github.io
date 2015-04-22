---
layout: post
title: twisted pb
categories:
- Programming Language
tags:
- Python&Lib
---

#Twisted Perspective Broker
---

##什么是PB?
- 字面意思是透明代理
- 包含两个方面：序列化、远程方法调用

##概念
- PBServerFactory:spread/pb.py
	- Factory类
- Broker:spread/pb.py
	- 作用类似protocol类
- RemoteReference:spread/pb.py
- pb.Root:spread/pb.py (twisted.spread.flavors.Root)
	- (被继承)
- pb.Referenceable:spread/pb.py (twisted.spread.flavors.Referenceable)
	- (被继承)可不用重写方法，直接定义远程调用方法--使用remote_做前缀
