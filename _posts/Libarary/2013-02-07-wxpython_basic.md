---
layout: post
title: wxpython basic
categories:
- Libarary
tags:
- python
- wxpython
---

# wxPython之基本概念
---
## 创建wxPython程序
### 创建程序主体的步骤：
- 导入必须的wxPython包
	- 必须先import wx模块进行必要的初始化，再import wxPython的其他子模块
- 子类化wxPython应用程序类
	- 也可以使用类库定义好的wxPython应用程序类
- 定义一个应用程序的初始化方法
	- 两种方式：__init__(self)，OnInit(self)，后一种方式更常见
	- 通常在OnInit()中定义Frame框架等必要的组件
- 创建一个应用程序类的实例
- 进入这个应用程序的主事件循环
	- 调用wx.App实例的MainLoop()方法，将控制权转交给wxPython
	- 不要阻塞事件主循环，其他任务可以放到其他线程中

### 创建窗口及控件的步骤:

### 绑定事件的步骤:

## 常用概念
### Appliction
- 每个wxPython程序必须有一个application用来执行消息循环等动作
- 系统定义的wx.App
	- wx.PySimpleApp
- 自定义的wx.App
	- 初始化方法__init__(self)，需要先调用父类的初始化
	- 常用初始化方法，OnInit(self)，return True：
		- 定义窗口等组件
	- SetTopWindow(frame)，可选操作，设置顶级窗口

### Frame
- Frame框架也被称为窗口，每个wxPython程序必须有至少一个frame对象。
- 顶级窗口，没有父容器的窗口部件
	- 至少必须有一个顶级窗口对象
	- 通过SetTopWindow()指定顶级窗口，否则顶级窗口列表中的第一个被默认为顶级窗口
- wx.Frame，所有框架的父类
- Dialog，可用来代替Frame,可认为是一个定义好的Frame
- wxPython的ID，所有窗口部件的特征：
	- 在wxPython中每个窗口都有一个ID标识
	- 在一个框架内必须唯一，而不同框架内部件的ID可重复－－尽管如此仍将是ID唯一
	- wxPython有部分预定义的ID，如wx.ID_OK,wx.ID_CANCEL等
	- ID的最重要作用是在指定的对象发生的事件和响应该事件的回调函数之间建立唯一的关联
	- ID的创建：
		- 明确的正整数
		- 使用wx.NewId()
		- 传递全局变量wx.ID_ANY或－1



- Window
- Panel
	- 放置在Frame中，每个Frame里至少有一个Panel
	- 用来控制布局的窗口
	- 其他控件/窗体，必须建立在Panel之上
- Sizer
	- 可使用Sizer进行定位，Sizer就像是一个布局用的容器




## wxPython对象
- wx.App应用程序对象
	- wx.App应用程序对象，不在GUI程序中显示，但管理GUI程序的周期和事件循环
	- \__init__方法:
		- 如子类重写则需调用父类的wx.App.\__init__()方法 －－不推荐子类重写该方法
		- 参数：self,redirect=Flase,filename=None,useBestVisual=False,clearSiglnt=True
	- OnInit方法：
		- 程序开始且主事件循环开始之前被调用
		- 参数：self,返回值为布尔值
		- 作用：
			- 做定制类的初始化操作--即创建GUI显示组件
			- 创建框架对象并Show()显示：
				- Show() == Show(True)
				- Hide() == Show(False)
			- 设定一个框架为顶级窗口：self.setTopWindow()
	- wx.PySimpleApp：系统定义的wx.App子类，不需要自定义wx.App子类
- 顶级窗口对象
	- wx.Frame的子类
		- wx.Frame框架是一个容器，可移动、缩放，包含标题栏、菜单等
		- wx.Frame类是所有框架的父类
		- wx.Frame中一般创建一个wx.Panel来容纳其他组件，在wx.Panel中可使用tab键来遍历组件儿wx.Frame不能
		- \__init__方法参数：
			- parent：父框架，对于顶级框架该值为None
			- id：新窗口的wxPython ID号，默认值-1表示由系统自动生成一个新的ID号
			- title：窗口标题
			- pos：一个wx.Point对象，新窗口左上角在屏幕中的位置，默认值(-1,-1)表示由系统决定
			- size：一个wx.Size对象，窗口的尺寸，默认值(-1,-1)表示由系统决定
			- style：窗口的类型，可由系统定义的多个常量组合：
				- 默认wx.DEFAULT_FRAME_STYLE，等价于：
					- wx.MAXIMIZE|wx.MINIMIZE|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX
				- 支持的操作：|(组合),^(去除)
			- name：框架内在名字，可通过名字来寻找该窗口
		- wx.Frame还包含菜单栏、状态栏、工具栏
	- wx.Dialog的子类

## 事件驱动
- 术语
	- 事件(event)
	- 事件对象：类wx.Event或其子类
		- wx.CloseEvent
		- wx.CommandEvent，窗口部件的各种交互：按钮单击、菜单项选择等
		- wx.KeyEvent
		- wx.MouseEvent
		- wx.PaintEvent，窗口内容需要重画时触发
		- wx.SizeEvent，窗口大小或布局改变时触发
		- wx.TimerEvent，由wx.Timer类触发，定时器
	- 事件类型
	- 事件源
	- 事件驱动
	- 事件队列
	- 事件处理器：响应事件时所调用的函数或方法：
		- 在wxPython中，任何能响应事件的对象都是wx.EvtHandler的子类
		- 所有窗口对象都是wx.EvtHandler的子类，wx.App也是
	- 事件绑定器：以wx.EVT_开头的全局变量
	- wx.EvtHandler：所有可显示对象的父类，有Bind()
- 事件驱动编程
	- 事件绑定，Bind(event,handler,source=None,id=wx.ID_ANY,id2=wx.ID_ANY)
	- wx.EvtHandler的其他方法
		- AddPendingEvent(event)，将event放入事件处理系统中，但不立刻触发，适用于多线程间基于事件的通信
		- Bind()方法
		- GetEvtHandlerEnabled()/SetEvtHandlerEnabled(boolean)
		- ProcessEvent(event)，把event放入事件处理系统中以便立即处理
	- Skip()方法
		- 事件的第一个处理器函数被发现并执行后，该事件终止
		- 通过在处理器返回之前调用该事件的Skip()方法，可允许该事件被其他处理器发现
	- 定制事件

## 常用类
- wx.Font
	- wx.Font(pointSize,family,style,weight,underline=False,faceName="",encoding=wx.FONTENCODING_DEFAULT)
	- family:
		- wx.DECORATIVE(老式英文字体),wx.DEFAULT,wx.MODERN(固定字符间隔)
		- wx.REMAN,wx.SCRIPT(手写体或草写体),wx.SWISS(sans-serif字体)
	- syle 倾斜：wx.NORMAL,wx.SLANT,wx.ITALIC
	- weight 加粗:wx.NORMAL,wx.LIGHT,wx.BOLD
- wx.Color
- wx.Point,point=wx.Point(3,3)
	- point.x   point.y
	- 可进行加、减和比较操作
	- 浮点型坐标：wx.RealPoint
- wx.Size,sizer=wx.Sizer(3,3)
	- sizer.weight sizer.height
- wx.Validator
	- 功能：验证控件中的数据；自动与对话框传递数据；验证用户键入的数据
	- 父类：wx.PyValidator
	- 子类覆写的方法：
		- \__init__(self)
		- Clone(self)
		- Validate(self,win)，验证控件数据方法
		- TransferToWindow(self)，控件打开时调用
		- TransferFromWindow(self)，对话框关闭时调用
