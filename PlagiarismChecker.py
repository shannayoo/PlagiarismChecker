#Plagiarism Checker
#Step 1: Open the input text file and handle it line by line to create a JSON file
#Step 2: Connect to Google's Search API and send a HTTP request
#Step 3: Receive the HTTP response and calculate the result to print it

import os
import pandas as pd
import datetime
import httplib2
from apiclient.discovery import build
from collections import defaultdict
from dateutil import relativedelta
import argparse
from oauth2client import client
from oauth2client import file
from oauth2client import tools
from TextFile import TextFile
from serpapi import GoogleSearch
url = "https://cse.google.com/cse?cx=3f408046cdd59f36c"
key = "AIzaSyDDXwViUWzNEmcepTV7EUk06KFpMQ-jnHA"
ClientID = "1098342281681-jmn8mg919ftok5hp86m1tblccf1mo042.apps.googleusercontent.com"
ClientSecret = "F5GgD4nm6L0iWkd432RyHc8d"

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

def search(q: str, api_key: str, ):
    parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[tools.argparser])
    flags = parser.parse_args([])
    
    flow = client.OAuth2WebServerFlow(client_id=ClientID,
                            client_secret=ClientSecret,
                            scope=SCOPES)
    site_list = webmasters_service.sites().list().execute()
    
    verified_sites_urls = [s['siteUrl'] for s in site_list['siteEntry']
                        if s['permissionLevel'] != 'siteUnverifiedUser'
                            and s['siteUrl'][:4] == 'http']
    
    for site_url in verified_sites_urls:
        print(site_url)     

                           

 
storage = file.Storage('searchconsole.dat')
 
credentials = storage.get()
if credentials is None or credentials.invalid:
  credentials = tools.run_flow(flow, storage, flags)
 
# Create an httplib2.Http object and authorize it with our credentials
http = credentials.authorize(http=httplib2.Http())


def _calculate_percentage(num: int, out_of: int) -> float:
    """ Simple function that returns the percentage. (num/out_of * 100)
    """
    try:
        percentage = (num/out_of) * 100
    except ZeroDivisionError:
        print("Number divided by zero")
    else:
        return percentage
