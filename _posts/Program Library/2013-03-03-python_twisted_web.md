---
layout: post
title: twisted web
categories:
- Libarary
tags:
- python
- twisted
---

#Twisted Web 编程
---

##概述
web处理可分为两部分：HTTP协议的解析和web请求的处理。  
HTTP协议是标准的互联网协议之一，可以进行高度的封装从而更集中处理web请求。  
web请求一般来说，有GET/HEAD/POST/OPTIONS/PUT/DELETE/TRACE等请求类型，其中GET/HEAD/POST最常用。

##低层次HTTP解析
HTTP协议建立在TCP之上，在该层的封装还有TCP框架的影子：

	# 相关类
	twisted.web.http.HTTPFactory	-- 对应Factory  
	twisted.web.http.HTTPChannel  	-- 解析HTTP协议，通过requestFactory可指定消息处理方法
	twisted.web.http.Request  		-- 消息处理，process()处理HTTP请求，
									-- setHeader()/setResponseCode()设置HTTP的状态字段

	# example code
	# file: requesthandler.py
	from twisted.internet import reactor
	from twisted.web import http

	class MyRequestHandler(http.Request):
		resources = {'/':'<h1>Home</h1>Home page','/about':'<h1>About</h1>All about me'}
		def process(self):
			self.setHeader('Content-Type','text/html')
			if self.resources.has_key(self.path):
				self.write(self.resources[self.path])
			else:
				self.setResponseCode(http.NOT_FOUND)
				self.write("<h1>Not Found</h1>Sorry,no such resource.")
			self.finish()

	class MyHTTP(http.HTTPChannel):
		requestFactory = MyRequestHandler

	class MyHTTPFactory(http.HTTPFactory):
		def buildProtocol(self,addr):
			return MyHTTP()

	reactor.listenTCP(8080,MyHTTPFactory())
	reactor.run()

##web请求处理
web请求处理是在HTTP解析之上做了进一步的封装。  
web请求流程：HTTP解析-->URL解析-->请求处理  
HTTP解析，处理HTTP协议头解析等  
URL解析，将URL(http://127.0.0.1:8080/foo/baz)分解为不同的segment(127.0.0.1:8080,foo,baz)  
请求处理：根据请求类型的不同进行相应的处理

###主要概念
- Site Object
	- 类似Factory作用，为连接请求创建HTTPChannel实例以解析HTTP请求
	- 使用Resource初始化，并将该Resource作为root Resource
- Resource
	- 实现IResource接口，代表URL中的一个独立的segment
	- 当URL结尾以反斜杠结尾时，getChild()中参数name为空，可在子类重写getChild()来处理该情况
- Resource trees
	- 以root Resource为根节点,解析URL时通过getChild()可遍历Resource tree
	- 通过putChild()可以添加Resource
	- leaf Resource：URL最后一个segment，Resource中isLeaf定义为True
- Resource rendering
	- 在render()中处理请求，返回结果可以是html字符串
	- 同步处理：调用request.write("stuff"),再调用request.finish()
	- 异步处理：定义Deferred并返回server.NOT_DONE_YET，在callback中调用request.wirte()和request.finish()
	- 使用默认的render()时可根据请求类型定义对应的处理：render_METHOD(render_GET,render_POST,render_HEAD)
- Session
	- 跨请求存储数据

###接口
	twisted.web.server.NOT_DONE_YET		-- 异步处理
	twisted.web.server.Site
	twisted.web.resource.Resource
		isLeaf							-- 是否是leaf Resource
		putChild(path,resource)
		getChild(self,name,request)
		render(self,request)
		render_METHOD系列：
			render_GET
			render_POST
			render_HEAD
	twisted.web.http.Request
		write("data")
		finish()
		uri,path,prepath,postpath		-- 路径相关，uri所有，path当前
		getSession()					-- 获取Session，如果没有就创建
		channel							-- 包含上级的HTTP协议对象
		transport						-- 通信对象
		method							-- HTTP方法，如GET/POST
		args							-- 请求参数
		content							-- 请求报文的实体主体，文件对象
		clientproto						-- HTTP版本
		received_headers,getAllHeaders(),getHeader(key)
		received_cookies,getCookie(key)
		client,getClient(),getClientIP()
		host,getRequestHostname(),getHost()
		getUser(),getPassword()
	
	twisted.web.static.File				-- 预定义文件Resource
	twisted.web.util.redictTo			-- 重定向

	# example code
	from twisted.internet import reactor
	from twisted.web import server,resource

	class ChildSimple(resource.Resource):
		isLeaf=True
		def __init__(self,id):
			resource.Resource.__init__(self)
			self.id=id
		def render_GET(self,request):
			return "Hello,No.%d visitor!"%self.id

	class Simple(resource.Resource):
		def __init__(self):
			resource.Resource.__init__(self)
			self.putChild("",self)
		def render_GET(self,request):
			return "Hello,world!"
		def getChild(self,path,request):
			return ChildSimple(path)
	
	reactor.listenTCP(8080,server.Site(Simple()))
	reactor.run()

###扩展
	twisted.web.vhost					-- Virtual Hosts
	root = vhost.NameVirtualHost()		-- root Resource
	root.default=static.File('/var/www/docs')
	
	root.addHost("foo.com",static.File("/var/www/foo"))