# Python专题之网络
---
## socket模块
- socket对象
	- socket.socket()返回socket对象
	- 参数：地址族(socket.AF_INET)，流(socket.SOCK_STREAM,socket.SOCK_DGRAM)，协议(默认0)
- socket对象方法
	- socket.bind(host,port)
	- socket.listen(num)
	- socket.accept()
	- socket.connect(host,port)
	- socket.connect_ex()
	- socket.recv(len)
	- socket.send(str)
	- socket.sendall()
	- socket.recvfrom()
	- socket.sendto()
	- socket.getpeername()
	- socket.getsockname()
	- socket.getsockopt()
	- socket.close()
	- socket.setblockiing()
	- socket.settimeout()
	- socket.gettimeout()
	- socket.fileno()
	- socket.makefile()

## urllib和urllib2模块
- urllib模块支持简单的下载，urllib2支持HTTP验证、cookie或扩展协议
- urllib模块方法：
	- urlopen(url) 返回的urllib对象，支持close\read\readline方法及迭代
	- urlretrieve(url[,location]) 获取远程文件，省略location则文件放入临时位置，用urlcleanup()负责清理