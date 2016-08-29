---
layout: post
title: Qt学习：model/view系统
categories:
- Qt
tags:
- Qt
- Library
---

> 用于展示数据(列表/表格/树)的框架

- 理解了框架的工作原理
- 定制自己的工作模块，然后运行框架

## model/view结构
> 三部分组成：model, view, delegate

- view，展示数据，主要方式：List, Table, Tree
	- 可以设置展示规则，如是否可编辑、表格的整行选择等
- model，数据，对不同数据源提供一个统一的数据接口
	- 除了数据，还提供一些展示的方式，如对齐方式等
- delegate，主要为视图提供两个高级功能：渲染和编译
	- 渲染，比如在表格单元格中展示图标等信息
	- 编辑，双击view中的展示数据可以提供编辑器

> 数据定位，在不同部分交流时的通用结构

- 模型索引，QModelIndex，提供行列信息来定位数据
	- 父节点，针对tree结构还需要提供父节点来定位
	- 模型在其它组件（视图和委托）请求时才会被创建
	- 索引保存有创建它的那个模型的指针，使得同时操作多个模型成为可能
		- 即在一个视图中展示多个模型的数据
- 数据角色，获取的数据是什么样的数据
	- 显示数据，用于在view中展示的数据
	- 展示数据，展示的样式，如左右对齐方式等

> 信号，框架中发生变化时出发信号

- 模型的信号提示底层维护的数据发生了变化
- 视图的信号提供了有关用户与界面进行交互的信息
- 委托的信号在用户编辑数据时使用，用于告知模型和视图编辑器的状态


---
## 使用
> 通过继承先定制自己的view/model/delegate，然后使用固定的流程

- 定义view对象
- 为view配置model和delegate

### 定制view/model/deletegate
> Qt提供了相应的继承类

- view，QAbstractItemView
	- 子类：QListView, QTableView, QTreeView
	- 特殊，QHeaderView提供表头功能
- model，QAbstractItemModel
	- 子类：QAbstractListModel, QAbtractTableModel
	- 预定义：QStringListModel, QFileSystemModel, QStandardItemModel
	- 数据库相关：QSqlQueryModel，QSqlTableModel，QSqlRelationalTableModel
- delegate，QAbstractItemDelegate
	- 子类：QItemDelegate，QStyledItemDelegate--推荐，支持Qt Style Sheet
	- 渲染功能接口：通过paint()和sizeHint()来渲染
	- 编辑功能接口：createEditor(), setEditorData(), updateEditorGeometry(), setModelData()


### 使用特例
> 视图选择，提供视图中的数据选择

- 获取视图中选择的数据
- 设置选中视图中的某些数据

> QSortFilterProxyModel

- 一个代理model，提供两方面功能：排序和过滤
- 使用：设置要代理的model，在view中设置model时使用代理model

---
## 相关图片
> 数据模型索引理解

![数据模型索引](https://raw.githubusercontent.com/yangdw/yangdw.github.io/master/_images/qt-series/model_view_2.png "数据模型索引")