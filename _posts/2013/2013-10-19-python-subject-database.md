#Python专题之数据库
---
> Python虽然没有标准的数据库模块，但定义了所有第三方模块必须遵守的数据库API

##数据库API
- 模块属性
	- apilevel，所使用的Python API版本
	- threadsafety，模块的线程安全级别
	- paramstyle，在SQL查询中使用的参数风格
- 数据库连接对象
	- connect(parameters...),返回数据库连接对象,参数有：
		- host,user,passwd,db,port,charset
		- unix_socket,conv,compress,connect_timeout
	- 链接对象：
		- close()
		- commit()，如支持就进行事务提交，否则什么也不做
		- rollback()，回滚事务
		- cursor(),创建游标对象
- 游标对象
	- 属性
		- arraysize，fetchmany中返回的行数，默认为1
		- connection
		- description，结果列表述的序列，只读
		- lastrowid
		- rowcount
		- rownumber
	- 方法
		- callproc(func[,args])
		- close()
		- execute(op[,args])
		- executemany(op,args)
		- fetchone()
		- fetchmany([size=cursor.arraysize])
		- fetchall()
		- next()
		- nextset()
		- setinputsize(sizes)
		- setoutputsize(size[,column])
		
## 常用数据库模块
- MySQL，mysqldb
- Oracle，cx_Oracle
- Redis