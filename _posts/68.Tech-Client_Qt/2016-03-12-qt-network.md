---
layout: post
title: Qt学习：网络
categories:
- Qt
tags:
- Qt
- Library
---

> 网络操作，主要是TCP通信和http通信

## TCP通信

---
## HTTP通信
> 主要类是QNetworkAccessManager

- 该类的设计是异步设计，不需要为网络特意开辟新的线程
- 网络请求返回QNetworkReply对象作为响应