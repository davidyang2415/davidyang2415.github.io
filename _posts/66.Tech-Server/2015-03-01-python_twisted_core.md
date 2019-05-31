---
layout: post
title: twisted基础
categories:
- Libarary
tags:
- python
- twisted
---

#Twisted基础
---
##事件驱动
事件驱动是除单线程服务、多线程服务之外的另一种消息处理模式，常见于UI编程中。  
事件驱动与回调一起使用，同时建议不要在回调函数中处理阻塞或耗时消息。

##核心对象
###Reactor
Twisted框架的核心，能够处理网络、文件系统和定时器事件。  
Reactor工作方式：等待事件发生，分类事件并将事件分派给注册的事件处理函数。

	while true:
		timeout = time_until_next_timed_event()
		events = wait_for_events(timeout)
		events += timed_events_until(now())
		for event in events:
			event.process()

函数接口：  
- **reactor.run()**  
- **reactor.stop()**  
- **reactor.listenTCP()**  
- **reactor.connectTCP()**  

###Transport
Transport是网络连接的细节。  
>接口函数：
  
- **write()**  
- **loseConnection()**  
- **getPeer()**  
- **getHost()**  

###Protocol
Protocol描述如何异步处理网络事件。Twisted包含了很多实现好的Protocol，如HTTP,Telnet,DNS和IMAP等协议。  
Protocol包含事件回调基础接口，包括连接的建立/断开、接收到新数据等。  
>接口函数:

- **makeConnection()**
- **connectionMade()**
- **dataReceived()**
- **connectionLost()**

###Protocol Factory
通过buildProtocol()为新连接创建Protocol--用于reactor注册回调。  
存储Factory创建所有的Protocol的公共数据、配置信息及公共处理函数。  
>接口函数：

- **buildProtocol()**

##Deferreds
> 帮助编写异步代码  
> 本身不能自动生成异步或非阻塞代码

Deferred对象就是一个回调集合，内部包含两个回调链--callback和errback。  
Deferred对象可作为参数和返回值进行传递，我认为这就是帮助编写异步代码的原因。

###使用步骤
1. 定义一个Deferred对象；  
2. 并定制回调链；
3. 通过callback()或errback()开始调用回调链。

###接口
> 定制回调链

- **addCallback()**
- **addErrback()**
- **addCallbacks()**
- **addBoth()**

通过addCallback()会在添加callback的同时会添加一个<pass-through>在errback链上。addErrback()同理。  
而addCallbacks()则会将callback和errback放在同一层中。  
回调链中，一层中的回调函数(callback或errback)会将返回值或无返回值时将参数传递给下一层对应回调函数处理。  
所以，回调函数中出现异常或错误后会调用在添加回调时后面的errback来处理。

> 调用回调

- **callback()**
- **errback()**

只有通过这两个接口才真正开始调用回调函数处理。


##Log
twisted.python.log使用流程：

###启动
**`log.startLogging(args)`**  
args是输出目标，可以是标准输出(sys.stdout或sys.stderr)，也可以是文件(open('filename','w'))  
也可以是twisted.python.logfile.LogFile('filename','path',rotateLength=100) # 100 bytes

###定制
**`log.addObserver(args)`**  
参数：  
继承log.FileLogObserver并重写emit(self,eventDict)方法，args参数为emit()方法  
实现log.ILogObserver，实现方法__init___(),__call__(self,eventDict)。

###记录
**`log.msg(),log.err()`**  
其中log.err()可以输出异常信息