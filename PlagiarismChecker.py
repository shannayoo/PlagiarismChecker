#Plagiarism Checker
#Step 1: Open the input text file and handle it line by line to create a JSON file
#Step 2: Connect to Google's Search API and send a HTTP request
#Step 3: Receive the HTTP response and calculate the result to print it

import os
from TextFile import TextFile
    
def filehandler(fn: fileIO) -> TextFile:
    """ Return an instance of TextFile with appropriate attributes by opening and reading fn.
    """
    # open and read fn
    try:
        f = open(fn, "r")
    except OSError:
        print("cannot open", fn)
    else:
        lines = f.readlines()
        f.close()

    # create and return an instance of TextFile
    new_text = TextFile(lines)
    return new_text

def _calculate_percentage(num: int, out_of: int) -> float:
    """ Simple function that returns the percentage. (num/out_of * 100)
    """
    try:
        percentage = (num/out_of) * 100
    except ZeroDivisionError:
        print("Number divided by zero")
    else:
        return percentage
