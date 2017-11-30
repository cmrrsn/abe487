#!/usr/bin/env python3
import os
import sys

args = sys.argv

if len(args) != 3:
    print('Usage: {} ARG1 ARG2'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

arg1 = args[1]
arg2 = args[2]

if arg1.isdigit() == True and arg2.isdigit() == True:
	ans = int(arg1)+int(arg2)
	print(ans)
elif arg1.isdigit() == False and arg2.isdigit() == False:
	print('{} and {}'.format(arg1, arg2))

else:
	print('Cannot combine number and string')
	sys.exit(1)
