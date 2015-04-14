---
layout:post
title:Python Object-Oriented
categries:
- Programming Language
tags:
- Python
---

# Python语法之面向对象
---
# 类：
- 新类与旧类
- 类定义：
	- class classname[(parentclass[,...])]:
		- varname = expr #定义在Class namespace
		- def metname(self[,...]):
- 创建类实例：
	- obj=ClassName(initargs...)
- python中新类型的类都是继承自object祖类
- 元类(metaclass)
- 类特殊属性：
	- __name__ ->str，类名
	- __doc__ ->str,类说明文档
	- __bases__ ->tuple,所有父类构成的元组
	- __dict__ -> 属性
	- __module__ -> 类所在的模块
	- __class__ -> 实例对应的类
- 调用父类函数：
	- super(ThisClass,self).methodname(args...)
	- ParentClass.methodname(self,args...)
- 特殊方法：
	- __new__(classref,initargs...)
	- __init__(self,initargs...)
	- __del__(self)
	- __repr__(self) ->str
	- __str__(self) ->str
	- __coerce__(self,other) ->value
	- __hash__(self) ->int
	- __getattr__(self,name) ->value,called for undefined attributes
	- __getattribute__(self,name) ->value,always called
	- __setattr__(self,name,value)
	- __delattr__(self,name)
	- __call(self,*args,**kwargs) ->value
	- __get__(self,obj,ownerclass)
	- __set__(self,obj,value)
	- __delete__(self,obj)
	- __copy__(self)
	- __deepcopy__(self,memo)
- 私有化
	- python不直接支持私有方式
	- 技巧是在私有化名字前加上双下划线，python会实现为_classname__method
- 其他
- 类定义，类实例化
- 数据成员与成员函数(方法)
- 类成员访问控制机制
- 类范围属性：静态类成员、类数据与类方法
- 特殊方法：构造函数、析构函数、复制函数、重载操作符函数
- 函数对象
- 内部类

## 继承
- 单继承与多继承
- 是否有祖类--如object类
- 继承访问控制
- 虚函数、纯虚函数
- 构造函数、析构函数的调用顺序

## 多态
- 类型转换
- 类方法在继承关系中查找顺序