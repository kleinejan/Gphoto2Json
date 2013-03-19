#! /usr/bin/python
# Filename: gPhoto2settingadmin.py

import datetime,re,json
import glob, os, fnmatch, time,sys,statvfs,json
from time import gmtime, strftime
from subprocess import Popen, PIPE

class gPhoto2setting(object):
	"""docstring for setting"""
	def __init__(self,config):
		super(gPhoto2setting, self).__init__()
		self.formObject=[]#
		self.config=config.rstrip()#stripoff spaces

		self.createObject()

	def createObject(self):
		gPhotoConfigList=self.config.split('\n')#Fetch var and Split it
		# FIXME CHECK THE INPUT FROM rstrip() when passing the CONFIG to this CLASS
		# it's fixed :) No need to Pop the Popsicle
		# gPhotoConfigList.pop() #Pops the last Empty line from Gphoto2		

		index=self.indexFinder(gPhotoConfigList)#index will now hold a list with index numbers
		i=0
		while i < len(index)-1: # need to strip 1 from the index to skip an Out of index error
			#	now we send a RANGE of the gphotoConfigList[0:4] to the renderSingle
			#	that will append a complete item to the formObject 
			item=self.renderSingle(gPhotoConfigList[index[i]:index[i+1]])
			self.formObject.append(item)
			i=i+1		

	def indexFinder(self,config):
		"""returns a list with INDEX numbers where each Config entry starts in the gPhotoConfigList
		example: indexList(0,4,14,18)
		each number represents a line starting with /main/group/settingname
		we need this to chop and slice the config into something usable
		"""
		indexList=[]
		for index,value in enumerate(config):
			if re.search('^/', value):
				indexList.append(index)#list with Index Number		
		return indexList

	def renderSingle(self,item):
			"""Slices every single config item into a nice Dictionary"""
			configVar		= item[0].split('/')
			settingPath		= item[0]
			settingItem		= configVar.pop()
			settingGroup	= configVar.pop()
			settingLabel	= re.sub('^Label: ', '', item[1])
			settingType		= re.sub('^Type: ', '', item[2])	
			settingCurrent	= re.sub('^Current: ', '', item[3])
			choiceList		= self.__dispatcher(settingType,item[4::])#get the forth value until the worlds ends
			settingCurrentIndex = self.__getValueFromIndex(settingCurrent,choiceList)
			dictList={
				'path':settingPath,
				'group':settingGroup,
				'name':settingItem,
				'type':settingType,
				'label':settingLabel,
				'current':settingCurrent,
				'currentindex':settingCurrentIndex,
				'options':choiceList
				}
			# self.formObject.append(dicto)#add item into the formObject
			return dictList

	def __dispatcher(self,type,optionList):
		"""Delegate what type we need to get back RANGE | MENU | RADIO
			and sends it to the specific function
		"""
		if(type=="RANGE"):
			value=self.__rangeBuilder(optionList)
		elif(type=="MENU"):
			value=self.__listBuilder(optionList)
		elif(type=="RADIO"):
			value=self.__listBuilder(optionList)			
		else:
			value=False
		return value

	def __rangeBuilder(self,optionList):
		"""build the range type
		currently the RANGE type is not yet supported. 
		"""
		listf=[]
		for i in optionList:
			value=re.search(r'((Top|Bottom|Step): )(.+)',i)
			if value:
				singleOption={value.group(2):value.group(3)}
				# listf+=(singleOption,)
				listf.append(singleOption)
		return listf

	def __listBuilder(self,optionList):
		"""Convert all CHOICE options into a Django Tuple"""
		listf=[]
		for i in optionList:
			 rawitem=re.sub('^Choice: ', '', i)	
			 value=re.search(r'([0-9]+)(\s)(.+)',rawitem)
			 if value:
				optionValue		= value.group(1)
				optionName		= value.group(3)
				singleOption	= {'index':optionValue,'name':optionName}

				
				listf.append(singleOption)
		return listf # a nested list of all Choices. Ideal for Django :)
	def __getValueFromIndex(self, current, dictList):
		
		if type(dictList) is list:
			for obj in dictList:
				# print type(obj)
				if obj.get('name')==current:
					return obj.get('index')
				
				
		
		# json.dumps(data)
		
			
		# return true
			# if item["classifiers"][0]["subcategory"] == "County"]
	
#def commander(cmd):
#	p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
#	out, err = p.communicate()
#	return out.rstrip()
#
#
#
#
#cmd = "gphoto2 --auto-detect | grep usb | cut -b 36-42 | sed 's/,/\//'"
#p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
#out, err = p.communicate()
#deviceID=out.rstrip()
#
#cmd2 = ("/home/janneman/usbreset /dev/bus/usb/%s") % deviceID
#p = Popen(cmd2 , shell=True, stdout=PIPE, stderr=PIPE)
#out, err = p.communicate()
#deviceID=out.rstrip()
#
#cmd = "gphoto2 --list-all-config"
#p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
#out, err = p.communicate()
## jan=base64.b64decode(out.rstrip()).decode('UTF-16')
#encoded = out.rstrip().encode('ascii')
#print commander(cmd)


#gphotoConfigVar = open('dummy.log', 'r').read()
#
#c=gPhoto2setting(gphotoConfigVar)
## c.machine()
#for i in c.formObject:
#	print i['label']
#	print i['current']
#	print i['choiceList']
# print json.dumps(c.formObject,indent=4,sort_keys=False)