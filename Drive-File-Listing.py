#! /usr/bin/env python

import os
import sys
import datetime

def main():
	f = open(/*Insert text file name*/, 'w')
	for root, dirs, files in os.walk(/*Insert path*/):
		for name in files:
			filename = os.path.join(root,name)
			s = filename + '\t' + root + '\t' + name + '\t' + str(datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(root,name)))) + '\n'
			f.write(s)
			print s
		
		
if __name__ == '__main__':
  main()