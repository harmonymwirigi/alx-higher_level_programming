#!/usr/bin/python3
# 2-append_write.py
"""
function that appends a string at the end of a text file (UTF8) 
and returns the number of characters added
Args:
     filename: the name of the file to be appended
     text: text to be appended

Return: the number of characters added
"""
def append_write(filename="", text=""):
    with open(filename, "a+", encoding = "utf-8") as f:
        f.write(text)
    return len(text)
