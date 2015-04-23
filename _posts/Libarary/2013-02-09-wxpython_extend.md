---
layout: post
title: wxpython extend
categories:
- Libarary
tags:
- python
- wxpython
---

# wxPython之扩展特性
---
## 扩展特性
- HTML支持
- 打印支持
- 剪贴板
- 拖拽功能
- 定时器wx.Timer
	- wx.Timer(owner=None,id=-1)
	- 事件：wx.EVT_TIMER
		- self.Bind(wx.EVT_TIMER,self.OnTimerEvent,self.timer)
		－ 事件方法：event.GetId()
	- 方法：SetOwner(owner=None,id=-1)，Start(milliseconds=-1,oneShot=False)
		- Stop()，IsRunning() IsOneShot()，GetInterval()
	- 扩展：继承wx.Timer类，需要覆写Notify()方法
		- wx.FutureCall(interval,callable,*args,**kwargs) 将来只调用一次
- 多线程