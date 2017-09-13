# -*- coding:utf-8 -*-  
import sys
import requests
import json
import traceback
import time
from requests.auth import HTTPBasicAuth
reload(sys)
sys.setdefaultencoding('utf-8')

class StarGit():
	# 获取用来点赞的账户列表: 数组 -> 字典(name, key)
	def getGitAccountList(self):
		list = [{'GitName': '用户名', 'GitPass': '密码'}]
		return list
	def getForStarUrl(self):
		return 'wang542413041/WangSwift'
	def getForFollow(self):
		return 'wang542413041'
	def star(self,url,acout):
		# global AUTH
		AUTH = HTTPBasicAuth(acout['GitName'], acout['GitPass'])
		requests.put("https://api.github.com/user/starred/"+url
			,headers={'Content-Length': '0'}
			,auth=AUTH)
	def follow(self, who, acout):
		# global AUTH
		AUTH = HTTPBasicAuth(acout['GitName'], acout['GitPass'])
		requests.put("https://api.github.com/user/following/"+who
		,headers={'Content-Length': '0'}
		,auth=AUTH)
SG=StarGit()
who = SG.getForFollow()
url = SG.getForStarUrl()
acounts = SG.getGitAccountList()
for acout in acounts:
	SG.star(url, acout)
	print "Stared! -->{}".format(acout['GitName'])
	time.sleep(5.0)
	SG.follow(who, acout)
	print "Follow! -->{}".format(acout['GitName'])
	time.sleep(5.0)