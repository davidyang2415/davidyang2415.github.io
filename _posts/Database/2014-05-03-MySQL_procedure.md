---
layout: post
title: MySQL存储过程
categories:
- Database
tags:
- Database
- MySQL
---

# MySQL存储过程
------------------
## 存储过程定义
### 定义语法
	DELIMITER $$
	CREATE PROCEDURE proc_name(IN n INT,INOUT io INT,OUT o INT)
	BEGIN
		...
	END
	$$

### 注释
- -- 中间要间隔一个空格，在(--)符号和注释之间最少要有一个空格  
- // 这是C风格注释  
- /\*这是多行注释\*/

### 流程控制
#### 条件:
	IF condition THEN
		...
	ELSE
		...
	END IF;  
#### CASE语句:
	CASE variable_name 
		WHEN val1 THEN ... 
		WHEN val2 THEN ... 
		ELSE ... 
	END CASE;  
#### WHILE循环:
	WHILE condition DO
		... 
	END WHILE;  
#### REPEAT循环:
	REPEAT ... 
	UNTIL condition
	END REPEAT;  
#### LOOP循环:
	LOOP LABLE:LOOP ...
	IF condition THEN leave LOOP_LABLE END IF;
	END LOOP;

### 游标
	DECLARE curname CURSOR FOR SELECT field1,field2,... FROM tablename;
	DECLARE CONTINUE HANDLE FOR SQLSTATE '02000' SET iStop=1;
	OPEN curname;
	WHILE iStop<>1 DO
		...
		FETCH curname INTO ifield1,ifield2,...
	END WHILE;
	CLOSE curname;

### 创建临时表
	CREATE TEMPORARY TABLE tabname(ID INT,Cnt INT);
	DROP TEMPORARY TABLE IF EXISTS tabname;

## 存储过程调用
