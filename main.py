#! /usr/bin/python

import datetime,re,json
import glob, os, fnmatch, time,sys,statvfs,json
from time import gmtime, strftime
from subprocess import Popen, PIPE
from Gphoto2Json import gPhoto2setting

gphotoConfigVar = open('gphoto2-config-input.log', 'r').read()

c=gPhoto2setting(gphotoConfigVar)
print json.dumps(c.formObject,separators=(',',':'),indent=4,sort_keys=True)
#for i in c.formObject:
#	print i['label']
#	print i['current']
#	# print i['currentindex']
#	print i['choiceList']
#	# print json.dumps(i['choiceList'])
