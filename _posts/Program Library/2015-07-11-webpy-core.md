---
layout: post
title: web.py功能点
categories:
- Libarary
tags:
- python
- web
---

## URL处理
- web.py提供两种URL映射方法
	- 正则映射：web.application(urls, globals())
		- 需要定义urls元组，关联URL与对应的消息处理类
		- URL部分使用正则表达式匹配
			- web.py会在内部给URL加上^和$
			- 数字(\d+),字符串(.*)
		- 消息处理类如果不在同一个文件中，需要指出具体路径
			- 如urls = ('/test','package.file.test')
		- 子程序中的路径是父应用剥离后的路径
	- 自动映射：
		- 先调用web.auto_application(),然后定义消息类就可以了
- 其他

## web.ctx
- web.ctx是线程安全的，保存每个HTTP请求的特定信息
- Request:
	- environ,有写作.env，包含标准WSGI环境变量的字典
	- home,应用的http根路径
	- homedomain,应用所在站点
	- homepath,当前应用所在路径
	- host,主机名+用户请求端口
	- ip,用户的IP地址，'xxx.xxx.xxx.xxx'格式
	- method,所有HTTP方法(GET/POST等)
	- path,用户请求路径
	- protocol,所用协议，如https
	- query,更在'?'字符后面的查询字符串
	- fullpath,可视为path+query，但不包含homepath
- Response:
	- status,HTTP状态码(默认'200 OK')
	- headers,包含HTTP头消息(headers)的二元组列表
	- output,包含相应实体的字符串

## session
- web.py在处理请求之前，就加载session对象；
	- 在请求处理完之后，会检查session数据是否被改动，如改动就交由session对象保存；
### 创建session:
     session = web.session.Session(app, web.session.DiskStrore('sessions'),initializer={'count':0})
          app，是web.application对象
          web.session.DiskStore('sessions')，硬盘存储session，也可以数据库存储
          initializer，初始化字典
### web.config中sessions_parameters保存着session的相关参数设置
默认设置如下：

	web.config.session_parameters['cookie_name'] = 'webpy_session_id'
	web.config.session_parameters['cookie_domain'] = None
	web.config.session_parameters['timeout'] = 86400, #24 * 60 * 60, # 24 hours   in seconds
	web.config.session_parameters['ignore_expiry'] = True
	web.config.session_parameters['ignore_change_ip'] = True
	web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
	web.config.session_parameters['expired_message'] = 'Session expired'
		* cookie_name - 保存session id的Cookie的名称
		* cookie_domain - 保存session id的Cookie的domain信息
		* timeout - session的有效时间 ，以秒为单位
		* ignore_expiry - 如果为True，session就永不过期
		* ignore_change_ip - 如果为False，就表明只有在访问该session的IP与创建该session的IP完全一致时，session才被允许访问。
		* secret_key - 密码种子，为session加密提供一个字符串种子
		* expired_message - session过期时显示的提示信息。
### 在调试下使用session：
使用web.py自带的webserver提供的web服务时，web.py就运行在调试模式下

     关闭调试模式：
          web.config.debug = False
     调试模式下使用session:
     import web 
     urls = ("/", "hello") 
     app = web.application(urls, globals()) 
     if web.config.get('_session') is None: 
          session = web.session.Session(app, web.session.DiskStore('sessions'), {'count': 0}) 
          web.config._session = session 
     else: 
          session = web.config._session 
     class hello: 
          def GET(self): 
               print 'session', session session.count += 1 
               return 'Hello, %s!' % session.count 
     if __name__ == "__main__": 
          app.run()



## 模板
- 模板是可使用python代码的HTML文件(包括.html和.xml两种)，
	- 一般定义在templates文件夹下
- 模板定义：
	- 定义模板接受的变量：$def with(name)
	- 可使用条件、循环等分支判断语句进行流程处理
	- 一般使用变量方式$name，如果变量含有格式则$:name会原始输出
- 模板最常使用方式(还有其他方式)：
	- render = web.template.render('templates/')
	- render.template_name(arg_name)
- 支持母模板：render = web.template.render('templates/', base='layout')
### 示例：
	$def with(name)
	$if name:
	I just wanted to say <em>hello</em> to $name
	$lse:
	<em>hello</em>,world!

## 数据库
- 连接数据库：
	- db = web.database(dbn='mysql', db='name', user='user', pw='password', host='ip', port=123)
- 查询：
	- result = db.select()
		- 参数：vars(用来填充查绚条件的变量),what(查询列名，默认*),where(条件),order(排序),
		- group(分组),limit(结果限制),offset(偏移量，从第几行开始),_test(查看运行时执行的SQL语句)
    - db.query("SELECT * FROM users WHERE id=$id", vars={'id':10})
	    - 返回值是一个iterbetter对象，是一个迭代器但不是列表，
		    - 内部维护着一个指向当前元素的指针，这个指针只会往后走，
		    - 即调用result[0]后，下次必须调用result[1]，再调用result[0]会抛出错误
		- 可以将返回值转换成List
- 更新：db.update()，参数同查询，返回更新影响的行数
- 删除：db.delete()，返回影响的行数
- 插入：db.insert(tablename, seqname=value)
### 事务处理：
	import web
	db = web.database(dbn="postgres", db="webpy", user="foo", pw="")
	t = db.transaction()
	try:
    	db.insert('person', name='foo')
	    db.insert('person', name='bar')
	except:
    	t.rollback()
    	raise
	else:
    	t.commit()

在python 2.5+以上的版本，事务同样可以在段中使用：
	from __future__ import with_statement
	db = web.databse(dbn="postgres", db="webpy", user="foo", pw="")
	with db.transaction():
    	db.insert('person', name='foo')
    	db.insert('person', name='bar')


## 扩展
- Application processors
	- 在处理请求之前或之后，通过添加处理器来完成某些操作
- web.background：
	- web.background和web.backgrounder都是python装饰器，
		- 让某个函数在一个单独的background线程中运行，
		- 而主线程继续处理当前的HTTP请求，并在稍后报告background线程的状态。
    - web.backgrounder不再发行版本中，而是在实验版本中，需要单独下载。

