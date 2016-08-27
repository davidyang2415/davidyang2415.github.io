---
layout: post
title: Qt学习：格式化文档XML与Json
categories:
- Qt
tags:
- Qt
- Library
---

## XML
- 读取，三种处理方式
	- 基于流：QtCore模块的QXmlStreamReader/QXmlStreamWriter类
	- DOM处理：主要类QDomDocument，一次性读取XML文件，在内存中建立XML树
	- SAX处理：主要类QXmlSimpleReader/QXmlDefaultHandler
- 写入
	-  QXmlStreamWriter的方式
	-  QDomDocument的save()方法

---
## Json
- 使用第三方模块QJson
- Qt5新提供的接口：
	- QJsonDocument,QJsonParseError
	- QJsonValue,QJsonArray,QJsonObject
	- QJsonObject::iterator


> Qt5新接口模式：

    QJsonParseError error;
    QJsonDocument jsonDocument = QJsonDocument::fromJson(json.toUtf8(), &error);
    if(error.error == QJsonParseError::NoError)
    {
		if(!(jsonDocument.isNull() || jsonDocument.isEmpty()))
        {
			if(jsonDocument.isObject())
            {     // TODO}
            else if(jsonDocument.isArray())
            {     // TODO}
        }
    }else{
		// 检查错误类型
    }
