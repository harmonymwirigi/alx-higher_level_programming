#!/usr/bin/python3
"""
function read_file to read the file file name
argr:
	filename : the file to be read
"""
def read_file(filename=""):
	""" with to ensure the file is closed after use"""
	with open(filename, "r", encoding = "utf-8") as f:
		f.read()
