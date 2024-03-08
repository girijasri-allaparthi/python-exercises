#!/usr/bin/env python3
import os
import requests
with open("/root/user/webpgm.txt") as file:
	fread=file.readlines()
#	print(fread)
	webdict={}
	for i in fread:
		if fread.index(i)==0:
			webdict['title']=i.strip()
		elif fread.index(i)==1:
			webdict['name']=i.strip()
		elif fread.index(i)==2:
			webdict['date']=i.strip()
		else:
			if fread.index(i)==3:
				webdict['feedback']=i.strip()
			else:
				webdict['feedback']=webdict.get('feedback')+' '+i.strip()
#	print(webdict)
listfiles=os.listdir()
print(listfiles)
print("added a testline1")
print("added a testline2")
