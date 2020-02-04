#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:13:53 2020

@author: Bamwani
"""
# Pythono3 code to rename multiple 
# files in a directory or folder 

# importing os module 
import os 
path_from = "/home/from/path/"
path_to = "/home/to/path/"
# Function to rename multiple files & STORE IN NEW FOLDER
def main(): 
	i = 0
	
	for filename in os.listdir(path_from): 
		dst =str(i) + ".jpg" # select file type
		src = path_from + filename 
		dst = path_to + dst 
		
		# rename() function will 
		# rename all the files 
		os.rename(src, dst) 
		i += 1

# Driver Code 
if __name__ == '__main__': 
	
	# Calling main() function 
	main() 
