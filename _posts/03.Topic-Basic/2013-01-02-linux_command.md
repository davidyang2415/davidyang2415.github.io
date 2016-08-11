---
layout: post
title: linux命令
categories:
- Tool Trick
tags:
- linux
---

> Linux命令就是可执行文件。

## 文件及文件夹操作
- ls
	- 常用方法：ls -al,a表示显示所有文件，l表示以长格式显示文件或目录的详细信息
	- 便利参数：h(文件大小更加易读),R(递归显示子目录),S(以文件大小排序),t(以更改时间排序)
- cd
- pwd：显示当前路径
- mkdir
- rm
- rmdir
- mv
- cp
- ln
- cat
- more
- less
- head
- tail

## 权限管理
- chmod
- chgrp
- chown

## 搜索
- find
- grep

## 压缩与解压缩
- tar
- gzip

## 磁盘
- df
- du

## 性能监控与优化
- ps
- top
- free

## 网络
- ifconfig
- ping
- netstat
- route
- telnet
- traceroute

## 工具类
- which
- whereis
- locate
- cal
- date
- diff
- wc


## 常用命令参数含义
- -a，all,archive(存档),append(附加)
- -b，blocksize(块大小),batch(批处理模式)
- -c，commands(执行命令),create(创建)
- -d，debug(调试),delete(删除),directory(目录)
- -e，execute(执行),edit(编辑),exclude(排除)
- -f， force(强制),file(文件),configuration file(指定配置文件)
- -g，
- -h，help(帮助),human readable(人性化显示),headers(头部)
- -i， interactive(交互模式),include(包含)
- -k，keep(保留),kill
- -l， long list format(长格式),list(列表),load(读取)
- -m，essage(消息),manual(手册),create home(创建home目录)
- -n，number(行号、编号),no
- -o，output(输出),options(选项)
- -p，port(端口),protocol(协议),passwd(密码)
- -q，quiet(静默)
- -r， reverse(反转),recursive(递归)
- -s，silent(安静),size(大小),subject(主题)
- -t， tag(),type(类型)
- -u，user(用户名、UID)
- -v，verbose(冗长),version(版本)
- -w，width(宽度),warning(警告)
- -x，exclude(排除)
- -y，yes
- -z，zip