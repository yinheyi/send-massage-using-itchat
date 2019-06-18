#! /usr/bin/python3.5
# -*- coding: utf-8 -*-

class BaseInfo:
	''' 该类为所有信息获取类的基类，定义了类的公共接口和默认的返回值。'''
	def GetContent(self):
		''' 该方法负责获取内容, 默认返回 I love China!'''
		return 'I love China!'

	def GetCreator(self):
		''' 该方法负责获取内容的创建者'''
		return 'yinheyi'

	def GetSource(self):
		''' 该方法负责获取内容的出处'''
		return 'it is from my heart.'

if __name__ == '__main__':
	test = BaseInfo()
	print(test.GetContent())
	print(test.GetCreator())
	print(test.GetSource())

