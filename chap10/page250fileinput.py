#!/usr/local/bin/python3
# preferable method to use for large files
# prerequisite : a file processmod.py must exist in the same directory

import fileinput, processmod

filename = 'page250.tx'
try:
    for line in fileinput.input(filename):
        processmod.process(line)
except Exception as e:
    print("Something went wrong while opening the file:", e)
