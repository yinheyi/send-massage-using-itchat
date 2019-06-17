#! /usr/bin/python3.5
# -*- coding: utf-8 -*-

'''
该模块负责从hitokoto网站获取一句话.
该模块只包含了一个HitoInfo类，该类有三个公开的方法，分别为：
GetContent(): 获取一言的内容
GetCreator(): 获取作者名
GetSource(): 获取出处。
'''
import requests

class HitoInfo:
	def __init__(self, url = 'https://v1.hitokoto.cn'):
		self.url = url			# 保存一言网的网址
		self.response = None 	# 保存json格式的https请求回应

	def GetContent(self, bFlush = True):
		'''
		该方法负责获取一言的内容, 参数bFlush是获取缓存还是重新获取新内容.
		a. 当bFlush为False时，它直接返回之前缓存下来的内容;
		b. 当bFlush为True时，它会重新请求网站，获取新内容;
		c. bFlush默认为True;
		'''
		if self.response ==None or bFlush == True:
			self.__GetResponse()
		return self.response['hitokoto']

	def GetCreator(self):
		' 该方法负责获取一言的作者, 该方法只返回之前缓存下来的信息. '
		if self.response == None:
			return '提示：请先获取一言内容，再获取作者信息!'
		else:
			return self.response['creator']

	def GetSource(self):
		' 该方法负责获取一言的出处, 该方法也同样返回之前缓存的信息. '

		if self.response == None:
			return '提示：请先获取一言内容，再获取来源!'
		else:
			return self.response['from']

	def __GetResponse(self):
		' a. 该方法负责对hikotoko进行https请求.  b. 该方法仅供类内使用.'
		# 网络请求异常代码有待补充
		temp = requests.get(self.url)
		self.response = temp.json()

# 实例化一个对象，供外部直接使用
HitoAnswer = HitoInfo()

if __name__ == '__main__':
	# 实例化一个对象
	test = HitoInfo()
	print('######################################')
	print('下面两条输出提示信息:')
	print (test.GetSource())
	print (test.GetCreator())
	for i in range(3):
		print('######################################')
		print('输出内容：')
		print (test.GetContent())
		print('######################################')
		print('下面两次的输出内容相同:')
		print (test.GetSource())
		print (test.GetSource())
		print (test.GetCreator())
		print (test.GetCreator())
