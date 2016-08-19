---
layout: post
title: MySQL数据库操作
categories:
- Database
tags:
- Database
- MySQL
---

## 定时任务
### 创建定时任务
	DELIMITER $$
	CREATE EVENT IF NOT EXISTS e_scheduleName	-- 任务名
	ON SCHEDULE EVERY 1 DAY STARTS '2014-04-01 23:59:59' -- 间隔时间，开始时间
	ON COMPLETION PRESERVE ENABLE -- 创建后是否生效
	DO BEGIN
		-- todo here! 定时任务内容
	END;
	$$

###  开启/关闭定时任务
- alter event e_scheduleName on completion preserve enable; -- 开启  
- alter event e_scheduleName on completion preserve disable; -- 关闭

### 定时任务查询
- show events; -- 显示所有定时任务
- show variables like '%sche%'; -- 查询MySQL系统是否开启定时任务功能  
- set global event_scheduler = 1; -- 开启MySQL系统的定时任务功能