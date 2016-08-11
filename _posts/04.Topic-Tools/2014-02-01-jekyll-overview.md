---
layout: post
title: 工具：jekyll，概述
categories:
- Tools
tags:
- jekyll
---

> 官网：http://jekyllrb.com/
> 使用github的个人主页时用到的技术

## 是什么？
> jekyll是一个生成静态网页的工具，作为blog生成工具。  
> 特点：可使用 markdown 来生成网页

## 目录结构
	index.html		// 主页
	_config.yml		// 配置文件
	_includes		// 页面标签，如页头、页脚等
	_layouts		// 布局模板
	_posts			// 发布文章
	_site			// jekyll生成的网页存放位置
	_drafts			// 草稿，个人创建

## 简单语法
> 具体语法需要查询官网，这里列出大概的提纲。  

	配置类语法：
		yml配置：指定项目的常用信息
		文章头信息：文章包括 html 和 md 两种文章
			信息给出文章的关联信息
	直接语法：
		是指在html和md中直接使用系统变量和语法来动态生成信息
		如 文章目录分页使用的 paginator 等

> 小提示：配置类中的格式，冒号后要有一个空格

## github创建个人主页
> jekyll最主要的使用就是在github创建个人主页了，过程大概为：

	A.创建github账号，生成相应的 name.github.io 库
	B.找到中意的jekyll类模板，并上传到库中
	C.学习简单的jekyll语法，更改模板
	D.写文章

> 以上步骤中A、B、C一般操作一次就完成了，剩下的就是专注写文章了