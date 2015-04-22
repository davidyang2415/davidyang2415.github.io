---
layout: post
title: google-glog
categories:
- Programming Language
tags:
- C++&Lib
---

# google-glog 开源库分析
---

## google-glog 开源库分析(一)：glog介绍  
本篇内容直接整理自官方文档及个人理解，如果可以建议直接查看[官方文档](http://google-glog.googlecode.com/svn/trunk/doc/glog.html)，

### glog是什么？
     Google glog is a library that implements application-level logging.
     This library provides logging APIs based on C++-style streams and various helper macros.

### glog主要内容
- 日志等级
	- 系统预定义等级：INFO(=0)<WARNING(=1)<ERROR(=2)<FATAL(=3)
	    - 以上是简写形式，可通过宏关闭简写形式，其原始定义是有GLOG_前缀
	    - 在windows中可能存在ERROR宏冲突的问题，通过宏监测会在编译器提示
	- 最严重级别是FATAL级别，对应DEBUG模式是DFATAL级别
		- 在输出FATAL日志消息后，会终止程序运行
		- DEBUG模式中，DFATAL级别对应ERROR--便于调试，而非DEBUG模式则对应FATAL
	- 每个级别都对应有相应的日志文件，日志文件的位置及名称定义如下：
		- 文件默认存放在临时文件中，windows下是"C:\Users\user_name\AppData\Local\Temp",Linux是"/tmp"
		- 文件名称：programname.hostname.user_name.log.severity_level.date.time.pid
		- Linux系还会创建为每个文件创建一个文件链接
	- 日志输出采用如下规则：
		- 每个级别的日志除了输出到对应日志文件中，还输出到每个低级别日志文件中
		- 如一个ERROR日志，会输出到INFO，WARNING，ERROR三个日志文件中
		- 默认，ERROR和FATAL消息除了输出到日志文件中之外，还会输出到标准错误中
- 符号变量
	- 通过符号变量可以定制日志行为
	- 设置符号变量的三个方法：
		- 系统装有google-fglags库，在安装google-glog时会自动使用google-fglags库
			- 可通过命令行参数来设置符号变量，如--logtostderr=1
			- PS:网上查找资料时看到内容：使用google-fglags库后vglgrind会提示内存泄漏(未验证)
		- 系统未安装google-fglags库，通过使用前缀"GLOG_"的环境变量可设置符号变量
		- 在程序中，通过修改全局变量(使用前缀"FLAGS_")来设置符号变量
			- 大多数符号变量修改后会立即生效
			- 与输出位置有关(如FLAGS_log_dir)，如果要生效需要在google::InitGoogleLogging()之前设置
	- 符号变量包括：
		- logtostderr(bool,default=false),只输出到STDERR而不写入日志文件
		- stderrthreshold(int,default=2,which is ERROR)，高于该级别的日志除写入日志文件还输出到STDERR
		- minloglevel(int,default=0,which is INFO)，低于该级别的日志消息不输出
		- log_dir(string,default="")，日志输出目录
		- v(int,default=0)，小于等于该值的VLOG(m)会被输出，否则不会输出
		- vmodule(string,default="")，可为源文件定制VLOG日志输出级别
		- max_log_size(int,default=1800)，日志文件最大值(单位MB)
		- log_link(string,default="")，日志文件的连接所在的文件夹
		- stop_logging_if_full_disk(bool,default=false)，如果磁盘写满是否停止记录日志
		- alsologtoemail(string,default="")，是否将日志额外发送邮件到指定地址
		- logemaillevel(int,default=999)，设置发送邮件的日志等级
		- logmailer(string,default="/bin/mail")，发送邮件程序
- DEBUG模式支持
	- DEBUG模式日志输出形式，增加前缀D表示DEBUG模式日志，如DLOG(log_severity),DLOG_IF(log_severity,condition)
	- 采用DEBUG宏控制，非DEBUG模式中DEBUG日志不会编译进程序就避免了程序冗余
- 丰富的助手宏
	- 所有助手宏中，因为有条件判断所以需要确认是否要将函数调用放在日志输出中
	- 条件宏:
		- LOG_IF(condition)
	- 计数宏:
		- LOG_EVERY_N(log_severity,num)
		- LOG_IF_EVERY_N(log_severity,condition,num)
		- LOG_FIRST_N(log_severity,num)
		- 使用google::COUNTER计数
	- 验证宏:
		- 功能类似assert断言，但不受DEBUG模式控制即非DEBUG模式也生效
		- 如果验证失败，会写FATAL日志并终止程序运行
		- CHECK(condition)
		- 比较验证：
			- CHECK_EQ(arg1,arg2)
			- CHECK_NE(arg1,arg2)
			- CHECK_LE(arg1,arg2)
			- CHECK_LT(arg1,arg2)
			- CHECK_GE(arg1,arg2)
			- CHECK_GT(arg1,arg2)
		- CHECK_NOTNULL(arg)
		- 字符串比较：
			- CHECK_STREQ
			- CHECK_STRNE
			- CHECK_STRCASEEQ
			- CHECK_STRCASENE
		- 浮点数验证：
			- CHECK_DOUBLE_EQ
			- CHECK_NEAR
		- 其中CHECK_NOTNULL不能作为日志输出流使用
		- 比较验证中，在输出中会输出比较值，所以要求比较值重载了输出操作符(operator<<(ostream,...))
		- 在验证宏中，参数会是匿名参数如CHECK(string("abc")[1],'b')
- 定制日志(Verbose Logging)
	- 目的：便于追踪不同的BUG，提供自定义日志级别
	- 级别控制：
		- 日志等级严重性与系统默认正好相反，大于-v设定级别的日志不会输出
		- 默认-v级别是0，级别可定义为负数
	- 日志输出：
		- 所有的VLOG宏日志消息都输出到INFO对应日志文件中
	- VLOG_IS_ON(n)使用：
		- 当n小于或等于-v设定的级别是返回true
	- 辅助宏：
		- 系统定义的辅助宏，都用对应的定制版本，需要加前缀V和更换系统日志级别为定制级别
- 特地的信号量处理
	- 针对可能导致程序崩溃的信号会输出dump信息
	- 处理的信号包括：
		- SIGSEGV,SIGILL,SIGABRT,SIGBUS,SIGTERM
	- 相关函数：
		- google::InstallFailureSignalHandler()
			- 信号处理函数
		- google::InstallFailureWriter(void (*writer)(const char* data,int size))
			- 默认dump信息输出到STDERR,可通过该函数定制dump输出目标
- 其他注意事项
	- 1.条件宏中，如果为假则右边日志中的函数不会执行
	- 2.默认FATAL日志和CHECK*宏会终止程序：
		- 默认会输出堆栈信息后以状态1退出程序
		- 可通过google::InstallFailureFunction(void (*func)())定制错误处理
	- 3.支持线程安全的日志Raw Logging，不分配内存和加解同步锁
	- 4.支持Google Style perror()，在系统日志宏前加前缀P，如PLOG(log_severity)
	- 5.支持Syslog,需要注意的是如果syslog配制为远程日志记录时的性能问题
	- 6.可通过GOOGLE_STRIP_LOG宏，在编译器就过滤掉不要的日志输出
		- 与符号变量minloglevel不用，该宏在编译器进行--即编译后的程序不可更改
		- 该宏同时会影响与INFO相关联的VLOGs日志
	- 7.windows平台，可能存在ERROR宏冲突问题，可通过禁用简短日志等级名称来规避


## google-glog 开源库分析(二)：glog用法

###glog使用
- 设置符号变量，定制日志行为
	- 具体符号变量的设置看glog介绍中的符号变量
- 日志系统初始化
	- 初始化函数：google::InitGoogleLogging(argv[0])
	- 初始化参数一般是第一个命令行参数--即程序的名称
- 结束时可以调用关闭日志系统函数
	- 关闭日志库函数：google::ShutdownGoogleLogging()
- 程序运行时，可通过命令行参数或环境变量来控制程序的日志行为

###glog APIs：
- void google::InitGoogleLogging(const char* argv0)
	- 初始化glog库，参数是第一个命令行参数即程序名
- void google::ShutdownGoogleLogging()
	- 关闭glog库
- void google::FlushLogFiles(LoSeverity min_severity)
	- [Thread-safe]指定级别以上的所有日志消息都立即写入到日志文件中
- void google::FlushLogFilesUnsafe(LogSeverity min_severity)
	- 非线程安全的输出指定级别以上的日志消息，用于灾难性程序问题时输出必要的日志消息
- void google::SetLogDestination(LogSeverity severity,const char* base_filename)
	- [Thread-safe]设置指定级别的日志输出的日志文件，如果base_filename为""则表示该级别日志不输出
- void google::SetLogSymlink(LogSeverity severity,const char* symlink_basename)
	- [Thread-safe]设置置顶级别的日志文件的软连接，symlik_basename为空表示不设置软连接
	- 如果不调用该函数，系统默认连接名称是程序名
- void google::AddLogSink(LogSink *destination)
- void google::RemoveLogSink(LogSink *destination)
	- [Thread-safe]添加和删除日志输出渠道
- void google::SetLogFilenameExtension(const char* filename_extension)
	- [Thread-safe]为所有日志文件添加文件扩展名，特别用于SetLogDestination()设置的日志文件
	- 通常做法是将监听的端口号作为日志文件扩展名
- void google::SetStderrLogging(LogSeverity min_severity)
	- [Thread-safe]确定除了输出到日志文件同时还输出到STDERR的日志最小级别
- void google::LogToStderr()
	- [Thread-safe]设置只只将日志输出到STDERR而不输出到日志文件
- void google::SetEmailLogging(LogSeverity min_severity,const char* address)
	- [Thread-safe]设置发送邮件的日志最小级别
- bool google::SendEmail(const char *dest,const char *subject,const char *body)
	- [Thread-safe]发送邮件
- const std::vector<std::string>& google::GetLoggingDirectories()
	- 获取日志输出目录集合
- void google::InstallFailureSignalHandler()
	- 信号处理函数，处理的主要信号有SIGSEGV/SIGILL/SIGFPE/SIGBRT/SIGBUS/SIGTERM
- void google::InstallFailureWriter(void (*writer)(const char *data,int size))
	- 设置系统崩溃时的输出函数，data数据不一定是以'\0'结尾
- void google::InstallFailureFunction(void (*fail_func)())
	- 设置LOG(FATAL)在输出日志消息后调用的函数


## google-glog 开源库分析(三)：glog核心类结构

### google-glog类核心结构
详见同目录下图片

### 工作原理
- 每个日志输出都对应一个google::LogMessage类对象
	- 构造函数中为日志添加必要的前缀：文件名、函数、时间、日志等级等信息
	- 析构函数中将日志消息写入到日志文件中
	- 每个google::LogMessage对象都持有一个定制的C++输出流及日志缓存
- 通过定制C++输出，实现日志的便捷输出
	- 继承自标准输入输出流，定制日志库使用的输出流--输出缓存在输出流对象初始化时提供
- 通过C++匿名对象的短生命周期性质，实现日志的自动输出
	- 通过宏会在日志输出时创建google::LogMessage匿名对象，该匿名对象会在行末分号处结束生命周期自动调用析构函数
- 内部提供统一的日志输出接口
	- 通过内部类LogDestination提供日志输出接口，其内部包含日志文件输出类对象
	- 日志文件输出对象是继承了Logger的LogFileObject对象，每个LogFileObject对象对应一个日志文件
	- LogDestination控制日志的输出，同时也控制日志文件的创建等行为

### 示例分析
- GLOG(ERROR)<<"hello,world!";
	- 根据宏定义:
		- #define LOG(severity) COMPACT_GOOGLE_LOG_ ## severity.stream()
		- #define COMPACT_GOOGLE_LOG_ERROR google::LogMessage(__FILE__,__LINE__,google::GLOG_ERROR)
	- 日志输出语句扩展为：
		- google::LogMessage(__FILE__,__LINE__,google::GLOG_ERROR).stream()<<"hello,world!";
- google::LogMessage(__FILE__,__LINE__,google::GLOG_ERROR)，创建一个匿名对象
	- 在构造函数中，创建日志输出流对象及日志缓存空间，并为日志添加必要的前缀信息
	- 日志输出流对象、日志缓存空间及日志状态标记等封装为google::LogMessage::LogMessageData结构
- std::ostream& google::LogMessage::stream()，方法stream()提供输出流支持
	- 通过操作符<<将日志消息输出到日志缓存中
- 行结尾分号处，匿名对象生命周期结束，调用析构函数
	- 在析构函数中，日志消息通过LogDestination类提供的静态方法接口写入日志文件

### 功能划分
通过以上分析可以看出，google::LogMessage类是基本骨架，构建了日志对象及输出通道  
具体的功能则有相应的类结构来完成，包括C++输出流及日志输出
#### C++输出流
- LogMessage::LogStream类，日志输出流对象
	- 继承自std::ostream，接收日志输出
	- 包含LogStreamBuf类数据成员
- LogStreamBuf，日志输出流缓存对象
	- 继承自std::streambuf，日志输出缓存
	- 本身不创建日志缓存区，构造函数时由参数传入内存区
- LogMessage::LogMessageData结构，每个LogMessage对象持有一个该结构对象
	- 包含LogMessage::LogStream类对象
	- 包含日志存储的内存区，用改内存区初始化LogMessage::LogSteam对象
	- 包含了日志的状体标记信息，如时间、等级、是否已经输出等信息
#### 日志输出
- Logger抽象类提供了日志输出接口，其子类LogFileObject是日志文件对象
	- 每个日志文件对应一个LogFileObject对象
	- LogFileObject对象提供日志文件的管理：创建新日志文件
- LogDestination类提供了日志输出接口
	- 通过静态方法，提供全局性的日志输出接口
	- 包含一个LogFileObject对象数组--每个日志级别对应一个日志文件
	- 除了日志文件之外，还提供多日志输出渠道：终端、邮件、系统日志等

## google-glog 开源库分析(四)：glog宏技巧
在核心结构之外，google-glog还通过宏技巧提供统一简洁的使用接口。  
同时，通过命名空间的使用尽可能的减少名字冲突，提供一个简介的日志库。  

### 宏助手
- 通过宏提供一个统一的简洁的日志输出接口
	- 简单的使用如LOG(INFO),LOG(ERROR)等日志输出接口
- 通过宏提供丰富的日志输出扩展功能
	- 提供了IF,CHECK等助手宏来简化代码

### 编程技巧
- 命名空间的使用
	- 因为是作为库使用，所以glog中使用了命名空间类避免名字冲突
	- 通过google命名空间提供glog库的接口空间，内部实现则进一步封装到嵌套命名空间中
- 宏技巧：分流
	- 通过DEBUG宏可将日志输出定位到LogMessage中还是什么也不输出的NullStream中
- 宏技巧：隐藏
	- 日志输出核心是通过LogMessage等类实现，同时通过宏提供了丰富的接口如条件日志，CHECK日志等
- 宏技巧：清洁
	- 在使用宏过程中，会在使用完成后进行#undef操作来保证库的宏不会干扰到使用库的程序
- 宏技巧：断言
	- 在mutex.h中，通过定义#define MutexLock(x) ...来保证同步锁不会出现MutexLock *lock=new MutexLock(&mu)之类错误
- 宏技巧：技巧
	- 1.在#if条件中使用# error,there is ... 直接输出错误消息的宏可在编译期间就给出错误提示
	- 2.在宏定义中使用do{...}while(0)来保证宏内容作为一个整体，避免出现宏展开时的问题：
		- 如#define call() a();b()，在调用if(1<0) call()时扩展成if(1<0) a(); b()后b()总是会被调用

### 小结
以上只是我参考了网上资料及阅读源代码时的总结，还没在实际项目中应用。  
通过阅读源代码，也是一种享受。