**功能说明**：该目录下的函数用于实现获取一些你准备使用itchat发送的消息。  
## 相关知识介绍
### 1. [requests](https://2.python-requests.org//zh_CN/latest/user/quickstart.html) 模块
- requests模块是python提供的基于网格请求的模块，其主要作用就是发送http请求。  
- 安装方法：`pip install requests`  
- 此处需要使用到的api:   
	1.  获取一个网页信息:  

	````
	my_url = 'www.baidu.com'
	response = requests.get(my_url)
	````

	2. 没了。

### 2. 从[一言网](https://hitokoto.cn/)获取每日一言  
- 一言网的api说明<https://hitokoto.cn/api>：

| 请求地址 | 请求方式 | 说明 | 
| :---: | :---: | :---: | 
|https:v1.hitokoto.cn/|GET//POST|站点QPS限制：10, 超过有可能会被民屏蔽|

- 返回参数(默认josn格式)说明:

|id|本条一言的id|
|:---:|:---:|
|hitokoto|一言正文，编码方式为utf-8|
|from|一言的出处|
|creator|添加者|
|created_at|添加时间|

例如：
````
	response = requests.get("https:v1.hitokoto.cn/")
	print response.json()
	
	# 输出为：
	id:240
	hitokoto:"有你在的日子才是我的日常。"
	type:"a"
	from:"琴浦小姐"
	creator:"红叶乘风我愿"
	created_at:"1468605916"
````
### 3. 
