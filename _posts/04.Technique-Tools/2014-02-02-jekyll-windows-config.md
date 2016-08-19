---
layout: post
title: 工具：jekyll，windows配置
categories:
- Tools
tags:
- jekyll
---

> 主要参考文章：http://blog.fooleap.org/run-jekyll-on-windows.html  
> 安装本地主要是便于本地调试

## 步骤
1. 安装 Ruby：  
	从官网(http://rubyinstaller.org/downloads)下载最新的稳定版Ruby，  
	在安装时要勾选 “Add Ruby executables to your PATH”，设置环境变量

2. 安装 Rbuy DevKit：  
     同一个官网，下载相应版本，运行后解压到目录(永久)，如C:\RubyDevKit  
     2.1. cd C:\RubyDevKit  
     2.2. ruby dk.rb init  
     2.3. 编辑2.2.生成的config.yml，添加 - C:/Ruby22-x64  
     2.4. ruby dk.rb install

3. 安装 Jekyll：  
	因为我是使用Github，所以安装的是github-pages  
	安装gem：gem install github-pages
  
     遇到的一个问题是，连接国外gem源出现问题，所以在网上找了国内源：  
          首先，taobao源不在可以使用，新的源是 https://gems.ruby-china.org/  
          其次，按照网站上的要求，先升级了gem版本到2.6  
          最后，因为遇到SSL证书问题，就直接使用的http而不是https  
       
          PS：第一次出现了错误，直接在运行一次就没有问题了  

## 问题
> gem源问题：

	首先，taobao源不在可以使用，新的源是 https://gems.ruby-china.org/  
	其次，按照网站上的要求，先升级了gem版本到2.6  
	最后，因为遇到SSL证书问题，就直接使用的http而不是https

> 启动：

	安装完成后，常用命令：
		查看版本：jekyll -v
		生成项目：jekyll new myblog
		运行：先进入项目目录，然后运行命令 jekyll serve

> window本地安装的相应库：

	安装rdiscount:gem install rdiscount
	安装pygments:gem install pygments.rb
	安装python对应模块：pip install pygments
	在_config.yml中添加配置：gems: [jekyll-paginate]