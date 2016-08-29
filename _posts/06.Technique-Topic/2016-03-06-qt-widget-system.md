---
layout: post
title: Qt学习：Widget体系
categories:
- Qt
tags:
- Qt
- Library
---

> QWidget提供了大量的组件用于桌面开发

- 窗口系统
- 布局管理器
- 对话框
- 与定义好的大量的组件

## 常用概念梳理
> 顶级窗口与非顶级窗口
  
- 顶级窗口：在任务栏有自己的位置  
- 非顶级窗口：在任务栏共享父组件的位置，默认出现在父组件的中心位置
- 指定父组件，即parent参数不为空则为非顶层窗口

## 常用类区分
- QMainWindow
- QWidget，是能够在屏幕上显示的一切组件的父类
	- 如果不确定，或者有可能作为顶级窗体，或有可能嵌入到其他窗体中，则基于QWidget创建
- QDialog
- QFrame

---
## 窗口系统
> 窗口，是指windows等平台上的常规窗口，Qt提供了QMainWindow

- 包括菜单、工具栏、状态栏、停靠区域等
	- 菜单和工具栏的操作一般抽象为QAction类
- 一般是继承QMainWindow来定制自己的窗口

### 布局管理器
> Qt的两种布局方式：绝对定位和布局管理器

- 绝对定位：给出坐标值和长宽值
	- 缺点是对于缩放不友好
- 布局管理器，根据规则自动排列
	- QHBoxLayout, QVBoxLayout
	- QGridLayout，在一个网格中进行布局，类似于HTML的table
	- QFormLayout，按照表格布局，类似于HTML的form
	- QStackedLayout，层叠的布局，将几个组件按照Z轴方向堆叠形成类似向导的效果

### 常用组件
> 输入，展示等

---
## 对话框
> 对话框的运行方式

- 模态：程序级别模态(QDialog::exec())，窗口级别模态(QDialog::open())
	- 模态会阻塞父组件(程序or窗口)的事件处理循环
- 非模态：QDialog::show()

> 从对话框获取数据

- 直接获取模态函数的返回值
	- 针对模态运行方式
- 可以关注对话框的信号

> 预定义对话框

	QMessageBox, QInputDialog
    QFileDialog, QPageSetupDialog
    QFontDialog, QColorDialog
    QPrintDialog, QPrintPreviewDialog
    QProgressDialog


> 预定义对话框通用使用方法

- 调用便捷的static函数
- 定义对话框对象，设置属性，调用运行


## 附件
> QMainWindow布局：

- ![QMainWindow布局](https://raw.githubusercontent.com/yangdw/yangdw.github.io/master/_images/qt-series/QMainWindow_layout.png "QMainWindow布局")