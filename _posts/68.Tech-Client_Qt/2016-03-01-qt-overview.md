---
layout: post
title: Qt学习：概述
categories:
- Qt
tags:
- Qt
- Library
---


> 使用Qt版本：Qt 5.4.2  
> 参考资料：[Qt学习之路2](https://www.devbean.net/category/qt-study-road-2),[Qt参考文档](http://www.kuqin.com/qtdocument/index.html)


## 跨平台常用的三种策略
- API映射：直接将平台的API映射为库接口，缺点是提供平台API最小集合，代表有wxWidget；
- API模拟：弥补API映射的不足，不提供的API功能由库提供，代表wine,DirectX；
- GUI模拟：使用平台基本的图形绘制函数，提供一套自己的组件库，代表有gtk+，Qt和Java的Swing;


## 关于Qt的一些问题
- 早期的Qt存在版权问题，但最近的版本则不存在该问题
- Qt提供很多特性的同时，相比于纯C++程序有一定的性能损耗--现代计算机可忽略不计