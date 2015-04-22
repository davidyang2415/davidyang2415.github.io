---
layout: post
title: linux shell
categories:
- Programming Language
tags:
- linux
---

#shell脚本基础
---

###输出
> echo

	echo "Hello,world!"
	echo 'Hello,world!'
	echo Hello,world!

- 三种表示法中，双引号和无引号形式中对特殊字符如分号需要使用转移格式；
- 输出变量时使用无引号形式；
- echo默认输出为一行；
- 支持彩色输出；
- 命令参数：
	+ 参数-e表示处理特殊字符：
		* \a(警报声),\b(删除前一个字符),\c(最后不加上换行符),\f(换行但光标停留原位置),
		* \n(换行且光标移至新行首),\r(光标移至行首但不换行),\t(插入tab),
		* \v(与\f相同),\\(插入\字符),\nnn(插入nnn(八进制)所代表的ASCII字符)
	+ 参数-n表示不换行输出

> printf

	printf "%-5s %-10s %-4s\n" No Name Mark

- 格式化输出时，换行需要使用'\n'；

###变量和环境变量
- 在Bash中，所有变量的值都是字符串--无论是否使用引号；
- 如果值中不包含任何空格，则不需要引号(单引号或双引号);
- 赋值(var=val)与相等(val1 = val2)的区别；s
- 通过前缀$可以打印输出变量的值:echo $var或echo ${var}；
- 获得变量(字符串)长度：length=${#var}

* 通过export命令设置环境变量；
* 常用环境变量：PATH,HOME,PWD,USER,UID,SHELL等；

###数字运算
> 适用于整数

	no1=4;
	no2=5;
	let result = no1+no2;
	let no1++;
	let no1+=6;

	result=$[no1+no2];
	result=$[$no1+5];
	result=$((no1-no2))

	result=`expr 3 + 4`;	# 不是单引号，是数字键1旁边的字符，叫做反引用符号
	result=$(expr $no1+5);

> 高级计算使用bc命令

###文件描述符和重定向
> 常用文件描述符

	0 -- stdin
	1 -- stdout
	2 -- stderr

> 重定向

- >等同于1>，先清空再写入，>>等同于1>>，追加到尾部；
- stderr重定向使用：2>形式，如果丢弃错误消息可以使用/etc/null作为重定向的文件；
- 使用 cmd < file 可以将文件重定向到命令；
- 通过 exec 3<input.txt 可自定义文件描述符；

###数组和关联数组
> 数组以整数做索引，关联数组可使用字符串做索引且从Bash4.0开始提供支持

	# 数组
	array_var=(1 2 3 4)
	array_var[10]=end	#(1 2 3 4 end)
	array_var[4]=5 		#(1 2 3 4 5 end)
	echo ${array_var[0]}
	index=3
	echo ${array_var[$index]}
	echo ${array_var[*]}
	echo ${array_var[@]}
	echo ${#array_var[*]}

	# 关联数组
	declare -A fruits_value
	fruits_value=([apple]='100 dollars' [orage]='150 dollars')
	fruits_value[banana]='80 dollars'
	echo "Apple costs ${fruits_value[apple]}"
	echo $(!fruits_value[*])


###别名
- 使用命令：alias install='sudo yum -y install'，可定义临时别名；
- 长久有效：echo 'alias install="sudo yum -y install"' >> ~/.bashrc；
- 另一种定义别名的方法是在~/.bashrc中定义一个别名函数；
- 在不信任环境是可以通过在命令前加\前缀来调用原始命令；

###终端信息
	#终端
	tput cols			# 显示行数
	tput lines			# 显示列数
	tput longname		# 显示终端完整名
	tput cup 100 100	# 将光标移动到(100,100)位置
	tput setb no		# 设置背景色，no可以使用[0,7]值替换
	tput setf no		# 设置前景色
	tput bold			# 设置粗体

	#输入密码
	#!/bin/sh
	#Filename: password.sh
	echo -e "Enter password: "
	stty -echo			# 关闭echo输出
	read password
	stty echo			# 开启echo输出
	echo
	echo Password read:$password

###日期与延时
	# 日期
	date		# 当前日期
	date +%s	# 当前时间的UNIX秒数
	date --date "Thu Nov 18 08:07:21 IST 2010" +%s #指定日期的UNIX秒数
	# 时间格式包括：%a,%A(星期),%b,%B(月),%d(日),%D(固定格式--mm/dd/yy),%y,%Y(年),
	#   %I或%H(小时),%M(分钟),%S(秒),%N(纳秒),%s(UNIX秒数)
	date "+%d %B %Y"
	date -s "格式化的日期字符串" # 设置日期和时间
	# 计算耗时
	#!/bin/bash
	#Filename: time_take.sh
	start=${date +%s}
	commands;
	statements;
	end=${date +%s}
	difference=$((end-start))
	echo Time taken to execute commands is $difference seconds.

	# 延时处理示例脚本
	#!/bin/bash
	#Filename:	sleep.sh
	echo -n Count:
	tput sc				# 存储光标位置

	count=0;
	while true;
	do
	if [ $count -lt 40 ];
	then let count++;
	sleep 1;			# 延时1秒
	tput rc				# 回复光标位置
	tput ed				# 清除从当前光标位置到行尾之间的所有内容
	echo -n $count;
	else exit 0;
	fi
	done


###调试脚本
> bash -x script.sh  
> 可下脚本中使用set -x显示参数与命令，使用set +x禁止调试；  
> 也可以在脚本第一行使用：#!/bin/bash -x；

###函数
	# 函数定义
	function fname()
	{
	statements;
	}
	fname()
	{
		$1 第一个参数
		$2 第二个参数
		...
		$n 第n个参数
		"$@" 扩展参数为"$1" "$2"等
		"$*" 扩展参数为"$1c$2c$3"形式，其中c是IFS(内部字段分隔符)的第一个字符
	}

	# 调用函数
	fname;
	fname arg1 arg2;

	# 导出函数
	export -f fname;

	# 获取函数返回值
	echo $?;

- Bash函数也支持递归调用；

###管道
	# 管道
	ls | cat -n		# 带行号的文件列表
	
	# 子shell
	cmd_output=$(ls | cat -n)
	cmd_output=`ls | cat -n`

	# 用子shell生成一个独立的进程
	pwd;
	(cd /bin;ls)
	pwd;


###read命令
	read -n 2 var	# 读取2个字符存放在var变量中
	read -s var		# 不回显方式读取密码
	read -p "Enter input:" var	# 带提示
	read -t 2 var 	# 在2秒内将键入的字符读入变量var
	read -d ":" var # hello: var被设置为hello，其中:是分隔符

###字段分隔符IFS
- 字段分隔符，即分割文本数据的分隔符，默认是空白字符(换行符、制表符或空格)；

###循环
	# for循环
	for var in list;	# list can be a string or a sequence
	do
	commands;
	done

	# 序列
	echo {1..10}
	echo {a..z}

	# c风格for循环
	for((i=0;i<10;i++))
	do
	commands;
	done

	# while循环
	while condition
	do
	commands;
	done

	#until循环
	until condition;
	do
	commands;
	done

###比较与测试
	# if
	if condition;
	then
	commands;
	fi

	if condition;
	then
	commands;
	elif condition;
	then
	commands;
	else
	commands;
	fi

	# 逻辑运算符
	[ condition ] && action;		# condition为真时执行action
	[ condition ] || action;		# condition为假时执行action
	[ $var1 -ne 0 -a $var -gt 2 ]	# -a表示逻辑与 
	[ $var1 -lt 0 -0 $var -gt 2 ]	# -o表示逻辑或

	# 算术比较
	[ $var -eq 0 ]	# 等于
	[ $var -ne 0 ]	# 不等于
	[ $var -gt 0 ]	# 大于
	[ $var -ge 0 ]	# 大于等于
	[ $var -lt 0 ]	# 小于
	[ $var -le 0 ]	# 小于等于

	# 字符串比较
	[[ $str1 = $str2 ]]		# 相等判断，注意=前后的空格
	[[ $str1 ==$str2 ]]		# 相等的另一个写法
	[[ $str1 != $str2 ]]	# 不相等
	[[ $str1 > $str2 ]]		# 大于
	[[ $str1 < $str2 ]]		# 小于
	[[ -z $str1 ]]			# 空字符串时返回真
	[[ -n $str1 ]]			# 非空字符串时返回真