---
layout: post
title: C语言标准库
categories:
- Programming Language
tags:
- C&C++
---

## I/O系统
- 头文件：#include <stdio.h>
- printf和scanf函数族
	- printf(),sprintf(),fprintf()
	- scanf(),sscanf(),fscanf()
	- vprintf(),vfprintf(),vsprintf()
- 输入与输出
	- 输入输出对象：标准设备(命令行)、文件、字符串
	- 常见操作：
		- 只适用于标准设备：getchar(),putchar(),gets(),puts()
		- fgetc()=getc(),fputc()=putc()=ungetc(),fgets(),fputs()
- 文件对象
	- FILE* fopen(const char\*,const char\*)
		- 通过返回值是否为NULL，判断文件打开是否成功
		- 同时可以按不同模式打开文件
	- 常用操作：
		- int fclose(FILE*)
		- int fflush(FILE*)
		- freopen()
		- fread()，通过判断读取的字符是否是EOF来判断是否到达文件尾(EndOfFile)
		- fwrite()
		- setbuf()
		- setvbuf()
		- int feof(FILE*)
		- clearerr(),ferror(),perror()
- 操作文件
	- remove()
	- rename()
	- tmpfile(),tmpnam()
- 二进制文件操作
	- 对于二进制文件，读写指针的位置有SEEK_SET,SEEK_CUR,SEEK_END来表示开始、当前和结尾的位置
	- 常用操作：
		- fgetpos(),fsetpos()
		- fseek(),ftell(),rewind()

## 字符与字符串
- 头文件：
	- 头文件：#include <stdlib.h>，类型转换函数
	- 头文件：#include <ctype.h>，类型判断函数
	- 头文件：#include <string.h>，字符与字符串操作函数
- 类型转换函数
	- atof(),atoi(),atol()
	- strtod(),strtol(),strtoul()
- 类型判断函数
	- isalnum(),isalpha(),iscntrl(),isdigit(),isgraph()
	- isprint(),ispunct(),isspace(),isxdigit()
- 字符与字符串操作函数
	- 字符大小写相关
		- islower(),isupper()
		- tolower(),toupper()
	- 内存函数
		- memset(),memcpy(),memmove()
		- memchr(),memcmp()
	- 字符串函数
		- strlen(),strcpy(),strncpy()
		- strcmp(),strncmp()
		- strcat(),strncat()
	- 字符串查找函数
		- strchr(),strrchr(),strnchr()
		- strspn(),strcspn(),strpbrk()
	- 分割字符串
		- strtok() -- 因为在内部使用的静态局部变量，所以存在并发问题
	- 其他
		- strcoll(),strerror(),strxfrm()

## 日期与时间
- 头文件：#include <time.h>
- 常用时间结构 struct tm
	- gmtime() GM:格林威治时间
	- localtime() 本地时间
- clock() ,单位1/1000s,程序运行时间
- time()  以参数或返回值方法获得当前时间点
- mktime() tm与time_t的转换
- 时间的格式化
	- asctime() struct tm转换为字符串
	- ctime() time_t时间点转换为字符串
	- strftime() 格式化字符串
- difftime() 时间间隔

## 数学
- 头文件：#include <stdlib.h>
	- abs(),fabs(),labs()
- 头文件：#include <math>
- ceil(),floor()
- div(),exp(),fmod(),frexp(),ldexp(),ldiv(),log(),log10(),modf(),pow(),sqrt()
- sin(),sinh(),cos(),acos(),asin(),atan(),atan2(),cosh(),tan(),tanh()

## 内存
- 头文件：#include <stdlib.h>
	- calloc(),malloc(),realloc()
	- free()

## 其他
- 头文件：#include <assert.h>
	- assert(),DEBUG下的断言
- 头文件：#include <stdlib.h>
	- abort(),exit(),atexit()
	- bsearch(),qsort()
	- rand(),srand()
	- system()
	- getenv()
- 头文件：#include <stdarg.h>
	- 可变参数相关:
	- va_arg(),va_start(),va_end()
- 头文件：#include <setjmp.h>
	- longjmp(),setjmp()
- 头文件：#include <singal.h>
	- raise()
	- signal()