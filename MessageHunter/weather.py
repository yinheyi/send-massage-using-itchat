#! /usr/bin/python3.5
# -*- coding: UTF-8 -*-

'''
本模块实现获取天气功能的类。
''' 
import requests
from BaseInfo import *

class weatherInfo(:
	def __init__(self):
		self.url = 'https://'
		self.response = None

	def __GetContent(self, bFlush = True):
