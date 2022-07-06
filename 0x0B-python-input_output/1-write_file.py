#!/usr/bin/python3
"""
function write_file writes into filename and insert text
Args:
	filename: the file to insert text
	text: the text to be inserted
Return:
	the number of characters inserted
"""
def write_file(filename="", text=""):
    """ creates the file if it doeas not exist """
    with open(filename, "w+", encoding = "utf-8") as f:
        f.write(text)
    """" read the file and returns the length"""
    with open(filename, "r", encoding = "utf-8") as f:
        line = f.read()
    return len(line)

