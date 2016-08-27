---
layout: post
title: Qt学习：文件系统
categories:
- Qt
tags:
- Qt
- Library
---


![Qt文件系统](https://raw.githubusercontent.com/yangdw/yangdw.github.io/master/_images/qt-series/file_system.png "Qt文件系统")


## 文件系统
> QIODevice，所有I/O设备类的父类，提供了字节块读写的通用操作及基本接口


     顺序访问设备：QProcess, QTcpSocket, QUdpSocket, QSslSocket
     随机访问设备：QFile, QTemporaryFile, QBuffer(读写QByteArray)

## 文件操作
> 文件读写提供了相应的读写接口，同时可使用流式操作  
> 格式化文件(XML/Json)则提供了专门的类处理


    QFile来表示文件
	QFileInfo来表示文件信息
    QDir表示路径信息

## 流式操作
- QDataStream：二进制流
- QTextStream：文本流
	- 自动将Unicode编码同操作系统的编码进行转换，包括换行符的转换
	- 使用16位的QChar作为基础的数据存储单元
	- 除了文件，也可以操作字符串
