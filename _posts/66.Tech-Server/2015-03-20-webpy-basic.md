---
layout: post
title: web.py基础
categories:
- Libarary
tags:
- python
- web
---

## 简介
web.py是一个轻量级的开源Python web框架。  
web.py的原作者(Aaron Swartz)已故，框架停留在0.3版本。

## 开发模板
	import web
	urls = (
		'/(.*)', 'hello'
		)
	app = web.application(urls, globals())

	class hello:
		def GET(self, name):
			if not name:
				name = 'world'
			web.header('Content-Type', 'text/html
			return 'hello,'+name+'!'

	app.run()

## 执行
- 使用web.py内置的web服务器运行
	- 测试时一般使用该方法
- 与nginx等web服务器组合使用：
	- web.py实现了WSGI--web服务器与应用程序之间的通用API

## 特殊变量
- web.input，可获得用户请求提交(GET/POST)的数据
	- 取的变量的web.storage对象(类似字典)
	- 可以在获取是指定默认值，如 data = web.input(id='no data')
	- web.input()取得的值都会被当作string类型
	- 多值变量参数，可以指定为list，否则会被当作一串而不是变量，如：
		- http://example.com?id=10&id=20
		- data = web.input(id=[])
- web.data()，从POST获取原始数据
- 跳转(seeother)与重定向(redirect)
	- 不支持0.3以下版本
	- 原理：服务器向浏览器发送一个303消息和新网址，
		- 浏览器会对新网址发送GET请求，完成跳转
    - 区别：web.redirect方法发送的是301消息--这是永久重定向，
	    - 适用于网站网址变更；

## 特殊处理问题
- 普通URL对应的消息处理类的GET方法是没有参数的，
	- 但是'/(.*)'对应的消息处理类的GET方法带有一个参数，就是获取的URL信息
- '/favicon.ico'，是在网页浏览器的地址栏和标签页显示的ICON图标