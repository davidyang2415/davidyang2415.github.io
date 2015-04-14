# Python语法之扩展特性
---
- Python高级特性包括：
	- 元类
	- 装饰器与闭包
	- 迭代器与生成器

##扩展特性
- 模板：
- 函数/方法修饰器：
	- 函数/方法修饰器实际上是函数，不过参数是被修饰的函数
	- 在被修饰的函数上一行以@开头，后跟修饰器函数和可选参数
	- 可用于在函数调用前先执行指定操作
- 可迭代对象
	- 可迭代对象接口：
		- next() -> next item
		- __iter(self)__ -> iterator object itself
	- 生成器
	- 使用步骤：gen=generatorfct(args),使用gen.next()获取值直到产生StopIteration异常

## 元类
- 基础：
	- 在Python中，类也是一种对象
- 理解：
- 用途：