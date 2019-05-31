---
layout: post
title: Java语法之高级特性
categories:
- Programming Language
tags:
- Java
---

## 类型信息
- RTTI(RunTime Type Information):
	- 在运行时识别对象和类的信息，包括传统的RTTI和反射机制；
	- 向下类型转换，多态中的类型识别；
- 类加载器，所有类第一次使用时动态加载到JVM中：
	- 首先确认类对象是否已经加载，如果没有加载则：
	- 先查找对应类名的.class文件
	- 加载类的Class对象到内存，在加载过程中会验证代码的正确性与安全性
	- 使用加载的Class对象创建该类的所有对象
- 初始化类过程：
	- 加载：查找字节码，创建Class对象
	- 链接：验证类中的字节码，为静态域分配存储空间，必须时解析类创建的对其他类的所有引用
	- 初始化：初始化超类，执行静态初始化器、静态初始化块
- 编译期常量的使用不会引起初始化
- Class对象：
	- Class对象，包含了与类相关的信息，即类型信息在运行时的表示
		- Class引用表示的是其所指向的对象的确切类型，而改对象是Class类的一个对象
	- 类是程序的一部分，每个类都有一个Class对象(信息保存在对应.class文件中)
	- 创建Class对象：
		- Class.forName(ClassNameString)，获取Class对象的引用并加载对应类
		- obj.getClass()，从对象获取其Class对象引用
		- ClassName.class，获取Class对象的引用但不会加载对应类
			- 编译期会进行检查，所以不需要用try{}catch(){}捕获
			- 适用于类、接口、数组以及基本类型，对应基本类型包装器的TYPE字段
	- Class对象常用方法：
		- Class.forName()
		- Class.newInstance()
		- Class.isInterface()
		- Class.getName()，Class.SimpleName()，Class.getCanonicalName()
		- Class.getInterfaces()，Class.getSuperClass()
	- 使用：
		- 普通的Class对象
		- 泛化的Class对象：<-目的是提供编译期类型检查
			- Class<Type>
			- Class<?>，等价于普通的Class对象，?表示"任何事物"
			- Class<? extends SuperClass>
			- Class<? super ClassName>
－ instanceof:
	- 返回boolean，类型验证
	- 限制：只可与命名类型做比较，而不能与Class对象做比较
	- 会考虑继承关系，即多态中字类也是基类的实例
- 反射：
	- 问题：
		- 普通RTTI要求在编译时编译器必须知道其处理的所有类
		- 对于编译后运行时出现的类，普通RTTI有限制
	- 实现：
		- Class类
		- java.lang.reflect库支持：
			- Field,Method以及Costructor
	- JVM运行时创建
	- 用处：
		- 对象序列化，JavaBean
		- 动态代理

## 泛型
- 泛型的核心概念：告诉编译器使用什么类型，编译器处理一切细节。
- 泛型的一个重要函数：简单而安全地创建复杂的模型，如数据结构
- 泛型，是针对足够复杂的问题的一种解决方案。
- 泛型的目标：
	- 更加通用的代码：多态 < 基于接口 < 泛型
	- 为容器类增加持有的类型
- 泛型定义：
	- 定义形式：class ClassName<A,B>{}
	- 支持继承和泛型接口
	- 泛型也可应用于内部类及匿名内部类
	- 局限：基本类型无法作为类型参数，解决方法是自动打包和自动拆包
- 泛型方法：
	- 定义：将泛型参数列表置于返回值之前
	- 使用：普通调用，由类型参数推断处理细节
		- 类型推断只对赋值有效
		- 可显示类型说明：点操作符与方法名之间插入尖括号，尖括号内饰类型
	- 泛型方法与可变参数列表能共存
- 深入理解泛型：
	- 擦除：在泛型代码内部无法获得任何有关泛型参数类型的信息，即具体类型信息被擦除了
		- new ArrayList<Integer>.getClass() == new ArrayList<String>.getClass()
	- 边界：针对擦除，使用边界告诉编译器更多类型参数信息
		- <T extends SuperClassName>
	- 擦除的目的：
		- 迁移兼容性：从非泛化代码到泛化代码的转变，兼顾现有非泛化代码
		- 泛型类型被当作第二类型处理，即不能再某些重要的上下文环境中使用的类型
	- 一个类不能实现同一个泛型接口的两种变体 <- 因为擦除的原因
- catch语句不能捕获泛型类型的异常
- 自限定：
	- class A extends SelfBounded<A>{}
	- class SelfBounded<T extends SelfBounded<T>>{}

## 注解