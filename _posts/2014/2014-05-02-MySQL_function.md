---
layout: post
title: MySQL函数
categories:
- Programming Language
tags:
- Database
---

# MySQL函数
------------------
- 主要包含两部分：
	- 系统函数
	- 自定义函数

## 系统定义函数
### 字符串函数
MySQL字符串下标，默认从1开始

- charset(str)
- length(str)
- strcmp(str1,str2)
- concat(str[,...])
- repeat(str,count)
- lcase(str),ucase(str)
- trim(str),ltrim(str),rtrim(str)
- instr(str,substr) -- 返回字串首次出现的位置，不存在时返回0
- locate(substr,str[,start_pos])
- substring(str,pos[,len])
- left(str,length),right(str,length) -- 从指定方向获取指定长度个字符
- replace(str,search_str,replace_str)
- prad(str,length,pad_str) -- 在str后用pad_str补充直到满足长度为length为止
- load_file(file_name)

### 数字函数
- rand([seed]) ,产生[0,1.0]之间的随机浮点数
- abs(num) ，绝对值
- ceiling(num) ，向上取整
- floor(num) ，向下取整
- round(num[],decimals) ，四舍五入
- format(num,decimal_palces) ，格式化数字，可将整数格式化为浮点数
- bin(decimal_num) ，十进制转二进制
- hex(decimal_num) ，十进制转十六进制
- conv(num,from_base,to_base) ，进制转换
- mod(num) ，取余
- power(num) ，指数
- sqrt(num) ，开平方
- least(num1,num2[,...]) ，求最小值

### 时间函数
- 常用时间格式：
	- %Y(4位),%y,%m,%H(24小时制),%h,%i,%S,%s
#### 获取日期与时间
- 获取时间戳：
	- now(),sysdate()--与now()区别，指定动态获取时间值
	- current_timestamp()/current_timestamp,localtime()/localtime
- 获取日期：
	- curdate(),current_date(),current_date
- 获取时间：
	- curtime(),current_time(),current_time
- UTC日期与时间：
	- utc_date(),utc_time(),utc_timestamp()
- Unix时间：
	- unix_timestamp(),unix_timestamp(date)
	- from_unixtime(unix_timestamp),from_unixtime(unix_timestamp,format)

#### 时间操作
- set @dt = '2014-04-05 12:12:12.123456';
- 直接选取  
	- select date(@dt),time(@dt),year(@dt),month(@dt),day(@dt),hour(@dt),minute(@dt),second(@dt),microsecond(@dt);  
	- select quarter(@dt),week(@dt); -- quarter,四分之一，一刻钟
- Extract()函数
	- select extract(year from @dt),extract(month from @dt),extract(day from @dt);
	- select extract(hour from @dt),extract(minute from @dt),extract(second from @dt),extract(mincrosecond from @dt);  
	- select extract(quarter from @dt),extract(week from @dt);  
	- select extract(year_month from @dt); 返回值格式为201404，其中year_month可替换成：  
		- day_hour,day_minute,day_second,day_microsecond,  
		- hour_minute,hour_second,hour_microsecond,  
		- minute_second,minute_microsecond,  
		- second_microsecond。
- dayof...系列：dayofyear(@dt),dayofmonth(@dt),dayofweek(@dt) -- 星期计算是：1=Sunday,...,7=Saturday
- week...系列：week(@dt),weekofyear(@dt),yearweek(@dt) -- yearweek()返回值是201413，其中13是第13周
- 日期名称：dayname(@dt),monthname(@dt) -- 返回英文名称
- last_day(@dt)，可计算指定月份有多少天

#### 日期时间转换
- time_to_sec('01:00:05),sec_to_time(3605)
- to_days('2014-04-05'),from_days(735693)
- str_to_date('08/09/2008','%m%d%Y'),str_to_date('08/09/08 08:09:30','%m%d%y %h:%i:%s')
- date_format('2014-04-05 12:12:30','%W %M %Y')
- makedate(year,dayofyear),maketime(hour,minute,second)

#### 时间运算
- 时间使用+/-运算符时存在不确定因素
- date_add()
	- 功能相同的不建议函数：adddate(),addtime()
	- select date_add(@date_var,interval 1 day);
		- year,month,day,hour,minute,second,microsecond
		- quarter(一刻钟),week
	- select date_add(@date_var,interval '1 01:15:30' day_second);
		- hour_second,day_second
- date_sub() ，与date_add()用法一致
- datediff(date1,date2)，返回相差天数
- timediff(time1,time2)，返回时间差值，time1和time2格式要相同且时间差有范围限制
- period_add(P,N),period_diff(P1,P2)，计算单位是月份

## 自定义函数
