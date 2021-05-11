#Plagiarism Checker
#Step 1: Open the input text file and handle it line by line to create a JSON file
#Step 2: Connect to Google's Search API and send a HTTP request
#Step 3: Receive the HTTP response and calculate the result to print it

import os

def filehandler(fn):
    f = open(fn, "r")
    lines = f.readlines()
    return lines
