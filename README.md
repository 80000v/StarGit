# StarGit
Git批量点赞加粉
<br/>这个脚本到底要不要放出来呢？！？！？！？！
```Python
for acout in acounts:
	SG.star(url, acout)
	print "Stared! -->{}".format(acout['GitName'])
	time.sleep(5.0)
	SG.follow(who, acout)
	print "Follow! -->{}".format(acout['GitName'])
	time.sleep(5.0)
```
