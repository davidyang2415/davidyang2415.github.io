---
layout: post
title: Qt学习：信号槽机制
categories:
- Qt
tags:
- Qt
- Library
---

> 信号槽机制是Qt的核心机制之一

## 是什么？
> 对象间的通信机制

- 从行为上类似于观察者模式：
	- 定义信号，关联信号与槽函数，触发信号来执行关联的槽函数
	- 一个信号可关联多个槽函数，一个槽函数也可管理多个信号
- 是C++函数回调的高级封装：
	- 信号和槽函数可以不在一个线程中执行

## 相关函数？
> 由QObject类提供的静态函数  
> 函数原型： connect(sender, signal, receiver, slot, type)

	// 一、使用函数名字符串
     QMetaObject::Connection connect(const QObject *,const char*, 
                                     const QObject *,const char*,
                                     Qt::ConnectionType);
     // 二、使用QMetaMethod子类
     QMetaObject::Connection connect(const QObject *,const QMetaMethod &,
                                     const QObject *,const QMetaMethod &,
                                     Qt::ConnectionType);
     // 三、使用函数指针
     QMetaObject::Connection connect(const QObject *,PointerToMemberFunction,
                                     const QObject *,PointerToMemberFunction,
                                     Qt::ConnectionType);
     // 四、receiver默认为this
     QMetaObject::Connection connect(const QObject *,const char*,
                                     const char*,
                                     Qt::ConnectionType) const;
	// 五、Functor接受static函数、全局函数及Lambda表达式
     QMetaObject::Connection connect(const QObject *,PointerToMemberFunction, 
                                     Functor);

- 接口说明：
	- 使用方式一的时候有要求：
		- 定义时使用slots宏，进而使用Q_OBJECT宏；
		- 使用时使用SLOT宏和SIGNAL宏
	- 方式四和方式五会提供编译期检查，而方式一在运行时才会发现错误
	- 方式四和方式五受public/protected/private的限制，private的槽函数只能内部关联
- 其他接口：
	- 对应解除关联函数是QObject::disconnect()
	- 在槽函数内部，使用sender()函数可获得发送信号对象

## 注意事项？
- 参数匹配与默认参数
	- 原则上槽函数中的参数必须有值
		- 信号参数数量比槽函数多
		- 虽然信号参数比槽函数参数少，但是缺少的参数提供了默认值也可以
	- 槽函数的参数与对应的信号的参数的类型必须一致
- 函数重载时编译器无法区分函数的问题
	- 通过定义函数指针来指明具体的函数