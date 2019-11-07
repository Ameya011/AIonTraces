import argparse
import glob
import os
from os import listdir, walk
from os.path import isfile, join
import re

# todo: fix pattern
file_pattern = "^(\d*)(-.*)$"

parser = argparse.ArgumentParser(description='Iterate over a folder of files.')
parser.add_argument('filepath', type=str,
                   help='file path to iterate over')

args = parser.parse_args()
print('File path: '+ args.filepath)


for root, dirs, files in os.walk(args.filepath, topdown=False):
   for name in files:
   	# print(os.path.join(root, name))
	timestampMatch = re.search(file_pattern, name)
	if timestampMatch:
		print(timestampMatch.group(1))
	
   # for name in dirs:
	# print(os.path.join(root, name))

