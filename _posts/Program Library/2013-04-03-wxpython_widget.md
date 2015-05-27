---
layout: post
title: wxpython控件
categories:
- Libarary
tags:
- python
- wxpython
---

## 基础窗口控件
### 静态文本StaticText
- wx.StaticText(parent,id,label,pos=wx.DefaultPosition,size=wx.DefaultSize,style=0,name='staticText'
- 样式
	- 对齐方式:wx.ALIGN_CENTER,wx.ALIGN_LEFT,wx.ALIGN_RIGHT
	- wx.ST_NO_AUTORESIZE 在使用SetLabel()后控件不会自动更改大小以适应新文本
- SetLabel(str) 设置新显示文本内容，未设定wx.ST_NO_AUTORESIZE样式时控件会自动扩展以适应新文本
- 事件：不接受也不响应鼠标事件
- 其他：wx.lib.stattext.GenStaticText

### 可编辑的文本TextCtrl
- wx.TextCtrl(parent,id,value="",pos=wx.DefaultPosition,size=wx.DefaultSize,
	- style=0,validator=wx.DefaultValidator,name=wx.TextCtrlNameStr)
- 样式
	- 单行文本样式
		- 对齐方式:wx.ALIGN_CENTER,wx.ALIGN_LEFT,wx.ALIGN_RIGHT
		- wx.TE_NOHIDESEL(只适用于windows，文本始终高亮显示),wx.TE_PASSWORD,
		- wx.TE_PROCESS_ENTER(文本内可使用Enter换行),wx.TE_PROCESS_TAB,wx.TE_READONLY
	- 多行文本样式
		- wx.TE_MULTILINE,wx.TE_AUTO_URL,wx.TE_HSCROLL,wx.TE_DONTWRAP(不换行,显示滚动条)
		- wx.TE_WORDWRAP(以单词为界换行,多数操作系统忽略),wx.TE_LINEWRAP(以字符换行,多数操作系统忽略),
		- wx.TE_RICH , wx.TE_RICH2 windows操作系统专用
- 方法：
	- 单行文本：
		- AppendText(text),Clear() 会生成一个文本更新事件,EnumlateKeyPress(event)
		- GetInsertionPoint(),SetInsertionPoint(pos),SetInsertionPointEnd()
		- GetSelection() 得到(开始索引，结束索引)的元组,GetStringSelection(),SetSelection(from,to)
		- GetRange(from,to),GetValue(),SetValue(value),Remove(from,to),Replace(from,to,value),WriteText(text)
	- 多行文本：IsMultiLine() , IsSingleLine(),GetNumberOfLines(),GetLineText(lineNo) , GetLineLength(lineNo)
- 事件：wx.EVT_TEXT,wx.EVT_TEXT_ENTER 处理wx.TE_PROCESS_ENTER,wx.EVT_TEXT_URL windows平台,wx.EVT_MAXLEN
- 其他：文本在控件中采用平台无关的换行符'\n'，而存储的字符串的换行符时分平台的

### 按钮Button
- wx.Button(parent,id,label,pos,size=wx.DefaultSize,style=0,validator,name="button"
- 方法：SetLabel(label),GetLabel(),SetDefaultSize(),GetDefaultSize(),SetDefault() 设为默认按钮－会获得焦点
- 事件：wx.EVT_BUTTON
- 位图按钮：wx.BitmapButton 显示位图替代文本
- 开关按钮：wx.ToggleButton wx.EVT_TOGGLEBUTTON事件，GetValue()和SetValue()设置二进制状态
- 通用按钮：wx.lib.buttons.GenButton

### 微调Slider
- wx.Slider(parent,id,value,minValue,maxValue,pos=wx.DefaultPosition,size=wx.DefaultSize,
	- style=wx.SL_HORIZONTAL,validator=wx.DefaultValidator,name='slider')
- 样式：
	- wx.SL_AUTOTICKS 刻度
	- wx.SL_HORIZONTAL wx.SL_VERTICAL
	- wx.SL_LABELS 显示数字标签(value,minValue,maxValue)
	- wx.SL_TOP wx.SL_LEFT wx.SL_RIGHT
- 事件：与窗口滚动条出发的事件相同
- 方法：GetRange() SetRange(minValue,maxValue)，GetTickFreq() SetTickFreq(n,pos) n表示刻度，pos设置成1就可以
	－ GetLineSize() SetLineSize(lineSize) 方向键移动的值，GetPageSize() SetPageSize(pageSize)
	－ GetValue() SetValue(value)

### 滑块SpinCtrl
- wx.SpinCtrl(parent,id=-1,value=wx.EmptyString,pos=wx.DefaultPosition,size=wx.DefaultSize,
	－ style=wx.SP_ARROW_KEYS,min=0,max=100,initial=0,name='wxSpinCtrl')
	－ 参数value无用设置为空字符串即可，用initial初始化默认值
－ 样式：wx.SP_ARROW_KEYS 允许使用键盘上下箭头键来更改控件值
	- wx.SP_WRAP 允许值循环
- 事件：wx.EVT_SPINCTRL 值改变时触发
- 方法：SetRange(minVal,maxVal) GetMin() GetMax()
	- GetValue() SetValue(value)

### 进度条Gauge
- wx.Gauge(parent,id,range,pos=wx.DefaultPosition,size=wx.DefaultSize,
	- style=wx.GA_HORIZONTAL,validator=wx.DefaultValidator,name='gauge')
- 样式：wx.GA_HORIZONTAL wx.GA_VERTICAL，wx.GA_PROGRESSBAR windows平台专用
- 事件：只读控件，没有事件
- 方法：SetRange(range) GetRange(),SetValue(pos) GetValue()

### 复选框CheckBox
- wx.CheckBox(parent,id,label,pos=wx.DefaultPosition,size=wx.DefaultSize,style=0,name='checkBox')
- 无样式
- 事件：EVT_CHECKBOX
- 方法：GetValue() SetValue(state)，IsChecked()

### 单选按钮RadioButton
- wx.RadioButton(parent,id,label,pos=wx.DefaultPosition,size=wx.DefaultSize,
	－ style=0,validator=wx.DefaultValidator,name='radioButton')
－ 样式：wx.RB_GROUP 标记之后的RadioButton时一组
－ 事件：wx.EVT_RADIOBUTTON

### 单选框RadioBox
- wx.RadioBox(parent,id,label,pos_wx.DefaultPosition,size=wx.DefaultSize,choices=None,majorDimension=0,
	- style=wx.RA_SPECIFY_COLS,validator=wx.DefaultValidator,name='radioBox')
- 样式；wx.RA_SPECIFY_COLS majorDimension指定的就是列宽度
	- wx.RA_SPECIFY_ROWS majorDimension指定的就是行宽度
- 事件：wx.EVT_RADIOBOX
- 方法：Enable() EnableItem(n,flag),GetCount() FindString(string),GetItemLabel(n) SetItemLabel(n,string)
	- GetSelection() GetStringSelection() SetSelection(n) SetStringSelection(string),ShowItem(item,showFlag)

### 列表框ListBox
- wx.ListBox(parent,id,pos=wx.DefaultPosition,size=wx.DefaultSize,choices=None,
	- style=0,validator=wx.DefaultValidator,name='listBox')
- 样式：
	- 选择样式：wx.LB_EXTENDED 可使用shift连续选择，wx.LB_MULTIPLE 可不连续多选，wx.LB_SINGLE
	- 滚动条样式：wx.LB_ALWAYS_SB，wx.LB_HSCROLL 默认
	- wx.LB_SORT 按字母排序
- 事件：wx.EVT_LISTBOX，wx.EVT_LISTBOX_DCLICK
- 方法：Append(item)，Deselect(n) 多重选择样式中取消位置n的选择，Set(choices) Clear()，InsertItems(items,pos)
	- GetString(n) SetString(n,string) Delete(n)，GetCount() FindString(string) Selected(n)
	- GetSelection() SetSelection(n,select) GetStringSelection() SetStringSelection(string,select) GetSelections()
- 扩展：wx.CheckListBox：
	- 构造函数和大多数方法与wx.ListBox相同
	- 新事件：wx.EVT_CHECKLISTBOX
	- Check(n,check) 设置位置n的选择状态,IsChecked(n)

### 下拉框Choice
- wx.Choice(parent,id,pos=wx.DefaultPosition,size=wx.DefaultSize,choices=None,
	- style=0,validator=wx.DefaultValidator,name='choice')
- 无专门的样式
- 事件：wx.EVT_CHOICE
- 几乎所有的ListBox的方法都适用Choice

### 组合框ComboBox
- wx.ComboBox(parent,id,value="",pos=wx.DefaultPosition,size=wx.DefaultSize,choices,
	- style=0,validator=wx.DefaultValidator,name='comboBox')
- 样式：wx.CB_DROPDOWN，wx.CB_SIMPLE windows样式，wx.READONLY，wx.CB_SORT
- wx.ComboBox是wx.Choice的子类

## 图像
- wx.Image
	- 与平台无关，装载和保存外部图像文件
	- wx.Image(name,type=wx.BITMAP_TYPE_ANY,index=-1)
	- 空图片：wx.EmptyImage(width,height)
	- 其他方法创建图像：
		- wx.ImageFromMime(name,mimetype,index=-1)
		- wx.ImageFromStream(stream,type=wx.BITMAP_TYPE_ANY,index=-1)
		- wx.ImageFromData(width,height,data)
	- 常用方法：
		- GetWidth() GetHeight()
		- Scale(width,height)--原图像不变 Rescale(width,height)－－原图像变化
		- Rotate90(clockwise=True)
- wx.Bitmap
	- 平台相关，显示图像
	- wx.Bitmap(name,type=wx.BITMAP_TYPE_ANY)
	- wx.EmptyBitmap(width,height,depth=-1)
	- 其他方法创建位图：
		- wx.BitmapFromImage(image,depth=-1)
		- wx.BitmapFromBits(bits,width,height,depth=-1)
		- wx.BitmapFromXPMData(listOfStrings)
- 图像展示容器：wx.StaticBitmap(parent,id,bitmap)

## 高级控件
### 启动画面
- wx.SplashScreen(bitmap,splashStyle,milliseconds,parent,id,pos=wx.DefaultPosition,size=wx.DefaultSize,
	- sytle=wx.SIMPLE_BORDER|wx.FRAME_NO_TASKBAR|wx.STAY_ON_TOP)
- 通常定义在wx.App子类的OnInit()或__init__()中
- 其后要跟wx.Yield()
