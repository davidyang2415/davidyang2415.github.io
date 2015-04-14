# python语法之内置容器
------------
Python中内建容器数据结构包括：序列、映射(如字典)及其他(如集合)。

## 序列
- 序列是一种概念，是具有相同行为特征的对象的抽象
- 内建序列：元组、列表、字符串、Unicode字符串、buffer对象和xrange对象
- 通用序列操作：
	- 索引：
		- 支持正负索引值，正索引从0开始到(len(seq)-1)
		- 负数索引，-1表示最后一个元素，-len(seq)表示第一个元素
	- 切片：
		- 切片得到的是新的对象，可用于获得序列的深拷贝 
		- 形式：seq[[start]:[end][:[step]]]
		- start,end支持正负数及其混用，切片范围包含start但不包含end，当start不在end左侧时得到空序列
		- start和end省略时表示开始位置和结尾位置的下一位，即seq[:]得到的是全元素复制
		- step默认值是1，负数表示反向步进
	- 操作符：
		- 同类型序列相加
			- 只有相同类型的序列才可以相加
			- 序列相加后等到新的序列对象
		- 序列乘法
			- 序列乘以数字n，表示序列被重复n次，获得的是新的序列对象
		- 成员资格
			- obj in seq 或 obj not in seq
	- 内建函数：
		- len(seq)
		- max(iter,key=None) 或 max(arg0,arg1,...,argN,key=None)
		- min(iter,key=None) 或 min(arg0,arg1,...,argN,key=None)
		- reversed(seq)
		- sorted(iter,func=None,key=None,reverse=False)
		- sum(seq,init=0)
		- zip([it0,it1,...,itN])
	- 迭代

## 元组(tuple)
- 创建元组：a=(),a=tuple()，单元组特殊表示：(1,)
- 元组是不可变序列
- 元组可看作是不可变的列表，但元组还是不可替代：
	- 元组可以在映射(如字典)中当作键使用
	- 内建函数和方法的返回值
		
## 列表(list)
- 创建列表：a=[] , a=list()
- 列表是可变序列
- 列表操作：
	- 元素赋值，更改列表
	- 删除元素，del seq[index]
	- 分片赋值，seq[start:end]=[number,...] 或seq[start:end]=[]
- 列表推到式
	- [ <expr1> for <k> in <list> if <expr2> ]
- 列表方法：
	- append(var) 追加到列表尾
	- cout(var) 统计var在列表中出现的次数
	- extend(anotherlist) 将anotherlist列表的元素按顺序添加到列表的尾部
	- index(var) var在list中的位置，找不到时抛出异常
	- insert(index,var) index超出列表范围时，index正数时插入到末尾，负数时插入到开头
	- pop() 返回最后一个元素并删除最后一个元素
	- remove(var) 找到var并删除，若无则抛出异常
	- reverse() 反向排列，改变列表对象
	- sort() 原有位置排序，更改列表对象

## 字符串(str)
- 字符串是不可变的
- 字符串定义：
	- 单引号、双引号、三引号
	- python字符串不是通过NULL或'\0'做结尾符来标记的
	- 转移字符
	- 格式化输出
		- 转换说明符含义：%[转换标志][最小字段宽度][精度]转换类型
			- 转换标志：-左对齐，+转换值前加正负号,空白符表示正数前保留空格，0表示转换值位数不够用0填充
			- 最小字段宽度：转换后的字符串至少应具有的宽度，*表示宽度从值元组中读取
			- 精度：点后跟精度值
			- 转换类型：
				- d,i,o,u,x,X,e,E,f,F,g,G
				- c,r,s
	- 前缀：
		- r/R 原始字符串，不进行转义
		- u/U Unicode字符串
- 一般在写入文件、数据库或网络时才使用encode()/decode()函数
- 字符串方法：
	- capitalize(),upper(),lower(),swapcase()
	- isalnum(),isalpah(),isdigit(),isupper(),islower(),istitle(),isspace()
	- find(substring[,start[,end]]),rfind(substring[,start[,end]])
	- index(substring[,start[,end]]),rindex(substring[,start[,end]])
	- count(substring[,start[,end]])
	- ljust(width),rjust(width),center(width)
	- lstrip(),rstrip(),strip()
	- join(seq)
	- split(words) -> list

## 映射，字典(dict)
- 字典是Python中唯一内建的映射类型。
- 定义：a={},a=dict()
	- 键值唯一，可以是数字、字符串和元组
- 字典可以应用于字符床格式化中
- 适用于字典的操作
	- len(d)
	- d[k]
	- d[k]=val	// 改变字典中键对应值，或自动添加新的键值对
	- del d[k]
	- k in d		// 成员资格
- 字典方法：
	- clear()
	- get(key,default=None)
	- has_key(key) ->True/False
	- items() ->list,列表元素是(key,value)
	- iteritems()
	- keys（）->list，包含键值
	- iterkeys()
	- values() ->list,包含值
	- itervalues()
	- update(dict2)
	- copy()
	- fromkeys(keys)
	- pop(key)
	- popitem()
	- setdefault(key,default)
