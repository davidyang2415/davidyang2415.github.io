---
layout: post
title: Qt学习：拖放与剪贴板
categories:
- Qt
tags:
- Qt
- Library
---

## 拖放
> 提供了一种能够在应用程序内部甚至是应用程序之间进行信息交换的机制

- 程序间拖放，常用的将文件拖拽到程序打开
- 程序内部组件的拖放

> 相关类及接口

- 事件
	- void dragEnterEvent(QDragEnterEvent *event)
		- 决定是否允许拖拽，以决定是否更改鼠标形状
	- void dropEvent(QDropEvent *event)
		- 拖放后的操作，即处理拖放的内容
- 设置组件的拖放属性，决定是否允许拖放

---
## 剪贴板
> 剪贴板由操作系统维护，所以由QApplication提供管理

- QClipboard *board = QApplication::clipboard()
	- board->setText("Text from Qt Application")
	- QString str = board->text()