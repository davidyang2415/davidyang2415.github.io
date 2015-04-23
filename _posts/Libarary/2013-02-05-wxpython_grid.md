---
layout: post
title: wxpython grid
categories:
- Libarary
tags:
- python
- wxpython
---

# wxPython之布局管理器
---
## 容器
- wx.Panel，其他空间的容器

### 复杂控件
- 网格grid

## sizer
- sizer是管理容器中的窗口部件的布局
- wxPython中的5个sizer
	- Grid
		- 规则的表格方式
		- wx.GridSizer(rows,cols,vgap,hgap) 0表示按实际计算，gap表示间隔
		- Add(window/sizer,proportion=0,flag=0,border=0,userData=None)
		- flag:wx.ALIGN_TOP wx.ALIGN_BOTTOM,wx.ALIGN_CENTER wx.ALIGN_CENTER_HORIZONTAL wx.ALIGN_CENTER_VERTICAL
			- wx.ALIGN_LEFT wx.ALIGN_RIGHT,wx.EXPAND,wx.FIXED_MINSIZE,wx.SHAPED
	- Flex grid:变化到每行和每列
	- Grid bag
	- Box
		- wx.BoxSizer(orient)
		- wx.VERTICAL wx.HORIZONTAL
	- Static box
- 使用sizer步骤
	- 创建并关联sizer到一个容器
	- 添加部件到sizer
	- 使sizer能够计算它的尺寸：父窗口的Fit()或sizer.Fit(window)
