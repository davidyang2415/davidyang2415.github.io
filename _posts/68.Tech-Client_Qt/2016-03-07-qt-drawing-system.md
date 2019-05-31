---
layout: post
title: Qt学习：绘图系统
categories:
- Qt
tags:
- Qt
- Library
---

> MainWindow-->canvas(Qt3)-->GraphicsView(Qt4)-->SceneGraph(Qt5),Qt绘图系统的演化史

## 概述
> 整个绘图系统基于QPainter,QPaintEngine,QPaintDevice

- QPaintDevice，绘制空间
	- 代表了可以在哪些地方进行绘制，具体看最后的图片
	- 处理常规设备之外，QWidget上也可以进行绘制
- QPaintEngine，统一接口
	- 对使用透明的，在QPainter和不同的QPaintDevice之间转换
- QPainter，绘制器
	- 提供大量draw*()函数进行绘制操作
	- 先设定绘制对象，然后进行绘制操作
	- 基于状态机机制，会保存最近一次的设定
		- 提供save()和restore()一对函数保存和回复状态

### 常用工具
> 画笔和画刷

- QPen，用于绘制轮廓线：样式、宽度、画刷、笔帽样式和连接样式等
- QBrush，用于填充：样式、颜色、渐变及纹理等

> 反走样

- 走样：由于采样不充分重建后造成的信息失真，就叫做走样
	- 在光栅图形显示器上绘制非水平、非垂直的直线或多边形边界时，或多或少会呈现锯齿状外观
- 反走样：用于减少或消除走样效果的技术，成为反走样
	- 图形学中的重要概念，很多系统的绘图API里都内置了有关反走样的算法
	- 由于性能问题，默认是关闭的，Qt也不例外

> 渐变

- 内置在Qt绘图系统中，在QBrush中设置
- 三种渐变：线性渐变(QLinearGradient)，辐射渐变(QRadialGradient)，角度渐变(QConicalGradient)

### 坐标系统
> QPainter的逻辑坐标与QPainDevice的物理坐标进行映射的工作

- 逻辑坐标，一般是指组件在父组件中的相对坐标
- 物理坐标，典型的如程序窗口在PC桌面上的坐标
	- 设备的左上角即坐标原点(0,0),x轴方向向右，y轴方向向下
- 由QPainter的变换矩阵、视口和窗口完成映射工作

> 坐标变换，变换的是坐标系

- 平移(translate)，旋转(rotate)，缩放(scale)和扭曲(shear)

---
## Graphics View Framework
> 包含一套完整的事件体系，可用于与场景中的元素进行双精度的交互

- 基于元素(item)的MV架构的框架：元素(item)，场景(scene)和视图(view)
	- 场景，QGraphicsScene，相当于整个世界
	- 视图，QGraphicsView，相当于照相机的取景框
	- 图形元件，QGraphicsItem，很多Qt内置的图形都继承自QGraphicsItem


## 图片
> QPaintDevice系统

![QPaintDevice](https://raw.githubusercontent.com/yangdw/yangdw.github.io/master/_images/qt-series/drawing-system.png "QPaintDevice")