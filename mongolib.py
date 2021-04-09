#! /usr/bin/env python

#################################################
# Author , Vishal Jagtap
# Script library functions and window functionality
#
# 2016-06-05     v1.0     :Initial release 
# 2021-04-09	 V1.0	  : Code pipeline trigger and store on AWS S3
#################################################

import sys
import subprocess
import os
import urllib2
import inspect
import re
#from lib.logger import logit
import logger

		
class mongolib_class:
	
	default_logdir="F:\pyhome\log\\"
	default_configdir="F:\pyhome\config\\"
	default_indir="F:\pyhome\in\\"
	default_outdir="F:\pyhome\out\\"
	default_moddir="F:\pyhome\bin\lib\\"
	
	
	def __init__(self,service,user,password,confile,ostype):
		self.service=service
		self.user=user
		self.password=password
		self.confile=confile
		self.ostype=ostype
		self.scriptname=sys.argv[0]
	
	def lineno(self):
		"""Returns the current line number in program."""
		return inspect.currentframe().f_back.f_lineno
	
	def service_start(self):
		if self.ostype == "W":
			try:
				output=os.system('net start MongoDB')
				#retval=subprocess.call(['runas', '/user:Administrator', 'net start MongoDB'])
				print retvalue
			except subprocess.CalledProcessError as err:
				print "error code",err.returncode,err.output
				
	def service_stop(self):
		retvalue=os.system('net stop MongoDB')
		#retvalue = subprocess.Popen("mongod --config F:/confile/mongo.conf")
		print retvalue
	
	def service_status(self):
		if self.ostype == "W":
			try:
				output=subprocess.check_output('sc query "MongoDB" | find "STATE"',shell=True)
				#retval=subprocess.call(['runas', '/user:Administrator', 'net start MongoDB'])
				status=output.split()
				if status[3] == "RUNNING":
					print "MongoDB service is Running"
				elif status[3] == "STOPPED":
					print "MongoDB service is Stopped"
					logger.logit(self.scriptname,'d','mongodb process stopped','E',self.lineno())
				else:
					print "MongoDB Service is in Unkown state"
			except subprocess.CalledProcessError as err:
				print "error code",err.returncode,err.output
				logger.logit(self.scriptname,'d','service status unknown error','E',self.lineno())
		elif self.ostype == "L":
			try:
				output=subprocess.check_output('sc query "MongoDB" | find "STATE"',shell=True)
				#retval=subprocess.call(['runas', '/user:Administrator', 'net start MongoDB'])
				status=output.split()
				if status[3] == "RUNNING":
					print "MongoDB service is Running"
				elif status[3] == "STOPPED":
					print "MongoDB service is Stopped"
					logger.logit(self.scriptname,'d','mongodb process stopped','E',self.lineno())
				else:
					print "MongoDB Service is in Unkown state"
			except subprocess.CalledProcessError as err:
				print "error code",err.returncode,err.output
				logger.logit(self.scriptname,'d','service status unknown error','E',self.lineno())
