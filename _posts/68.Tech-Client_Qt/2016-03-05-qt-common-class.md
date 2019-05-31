---
layout: post
title: Qt学习：常用类
categories:
- Qt
tags:
- Qt
- Library
---

## 基础类型
> 整数系列：有符号与无符号区别

- qint8, qint32, qint64
- quint8, quint32, quint64
- uchar, ushort, uint, ulong

> 浮点数系列

- qreal， 默认实现为double，也可以通过宏实现为float

> 指针系列

- qintptr, quintptr, qptrdiff

## 核心类
> 这部分类是Qt的核心，也是最常用的类

- QObject
- QString， Qt在标准C++之上的封装扩充
- QVariant
- QCoreApplication/QApplication
- 其他：QByteArray

## 常用GUI类
> GUI操作中对于常用概念(坐标点、矩形等)的封装

- QPoint/QPointF
- QRect/QRectF
- QBitmap, QImage, QPicture
- QPixmap，专门为图像在屏幕上的显示做了优化
- QPainter
- QPainterPath

## 容器
> Qt的容器类都不继承QObject

### 容器类型
> 顺序容器

- QList
	- QQueue，先进先出(FIFO)
	- QStringList，内部数组实现
- QLinkedList，适用于中间插入大量数据
- QVector
	- QStack，后进先出(LIFO)
- QSet


> 关联容器

- QMap, QMultiMap
	- 带有Multi的容器支持一键关联多值
- QHash, QMultiHashMap
- QCache, QContiguousCache
	- 在有限缓存空间中提供高效Hash查找

> 特殊说明：

	容器中存储的类型必须是可赋值数据类型：
		基本数据类型
		具有默认构造函数、拷贝函数和赋值运算符的类型
		QObject及其子类(QWidget,QTimer等)不具有可赋值性，变通是使用指针
	使用关联容器要求：
		QMap必须提供operator<()重载
		QHash提供operator==()重载和一个名字是qHash()的全局函数


### 容器操作
> 遍历容器，方式

- STL风格，使用迭代器
	- 只读需求，强烈推荐使用const类型迭代器，由隐式数据共享特性决定更高效
- Java风格
	- 相关函数 hasNext(), next()等
- 迭代器
	- 只读(QListIterator,QLinkedListIterator,QVectorIterator,QSetIterator,QMapIterator,QHashIterator)

> 遍历容器，Qt版foreach关键字，不同于C++ 11的foreach

- foreach(type iter,connection)...

### 容器的特性
> 隐式数据共享、不可变特性、线程安全、平台无关

#### 隐式数据共享
> 本质上是一种内存对象管理技术

- 通过引用计数器来减少不必要的拷贝操作
- 写时复写：有写需求时才会对对象进行深拷贝操作

> 对使用上的影响

- 对于使用基本是透明的
- 对于QList或QVector，使用at()而不是[] -- 进行使用右值
- 遍历容器时使用const类型的迭代器