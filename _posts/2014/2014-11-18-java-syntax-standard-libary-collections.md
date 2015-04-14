---
layout:post
title:Java Collections
categries:
- Programming Language
tags:
- Java
---

# Java语法之标准库之容器篇
--------------------------------------
## 常遇到问题
- 遍历容器时，插入和删除元素

## 容器基础
- 不必创建命名来持有每一个对象
- 持有的对象数量不固定，可动态调整
- 每种容器都有自己的规则
### 容器与泛型
- 创建容器时，需要指定容器中对象的类型
- 通过泛型，可在编译期防止将错误类型的对象放置到容器中
- 多态也可用于容器，即指定类型的子类也可放入到容器中
### 迭代器
- 获取迭代器
	- 容器的iterator()方法可返回该容器的迭代器对象
- 常用操作
	- hasNext(),next(),remove
- 特定迭代器
	- ListIterator，只用于各种List类的访问，是Iterator的子类
		- 可双向移动
### 容器特性
- Array，顺序存放
- Linked，便于插入和删除
- Hash，快速查找
- Tree，顺序

## 通用容器
### 容器工具类
- 容器工具类提供了可用于容器的很多使用方法。
#### Arrays
- Arrays.asList()
	- 返回的结果list,是内部实现的list，底层实现的是数组，不能动态扩展
	- 使用的是不固定参数，如果传入的是数组(如int[])，返回的不是List<int>
#### Collections

### 序列类容器
- Collection
#### List
- ArrayList
- LinkedList
#### Set
- HashSet/LinkedHashSet
- TreeSet
#### Queue
- Queue是接口，LinkedList实现了Queue接口
- PriorityQueue

### 关联容器
#### Map
- HashMap/LinkedHashMap
- TreeMap

### 遗留构件
- Vector
- Stack
- HashTable

## 并发容器