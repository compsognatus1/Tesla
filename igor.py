#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import signal
import subprocess
import unicodedata
import time
import sys
from random import randint
from DTCScrapper import DTCScrapper

class Bot():
	
	def __init__(self):
		self.name = 'Igor'
	def start(self) :
		print 'Ouiiii maiiiiitre'
		time.sleep(1)
		cmd ='terminator -x python tesla.py'
		self.process_compress = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid) 
		exec ('exit')
if __name__ == "__main__":		
	Bot().start()
