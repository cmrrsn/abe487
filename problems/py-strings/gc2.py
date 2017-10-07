#!/usr/bin/env python3

import sys
import os


def main():
	"""main"""
	
	files = sys.argv[1:]
	if len(files) != 1:
		print('Usage: {} FILE' .format(sys.argv[0]))
		sys.exit(1)
	if os.path.isfile(files[0]) == False:
		print('"{}" is not a file'.format(files[0]))	
		sys.exit(1)	

	for seq in open(files[0]):
		i=0
		gc=0
		for bp in seq:
			if bp in 'aAtTcCgG':
				i += 1
			if bp in 'gGcC':
				gc += 1
		pgc = int((gc/i)*100)
		print('{}'.format(pgc))		

if __name__ == '__main__':
	main()
