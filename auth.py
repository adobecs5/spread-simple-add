#-*- coding: utf-8 -*-
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

def authorize(jsonPath = None, spreadName=None):
    '''
    :param jsonPath: Path of Json credentials. Refer to http://gspread.readthedocs.org/en/latest/oauth2.html
    :param spreadName: Name of spreadsheet
    *** you must do step 7 of http://gspread.readthedocs.org/en/latest/oauth2.html
    :return:
    gc - whole spreadsheet
    wks - working spreadsheet
    '''
    if jsonPath == None:
        json_key = json.load(open("SpreadSheet-c1ee45e28fe7.json"))
    else:
        json_key = json.load(open("jsonPath"))
    scope = ['https://spreadsheets.google.com/feeds']

    credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
    gc = gspread.authorize(credentials)
    # Change below "sheet1" to move along sheets
    if spreadName == None:
        wks = gc.open("example1").sheet1
    else:
        wks = gc.open(spreadName).sheet1
    print ("successfully loaded: %s"%wks.title)

    return gc, wks

def open_a_spreadsheet(gc, key, type = None):
    '''
    :param gc: gc.
    :param key: ket could be of 3 types. name, key, and url.
    name is clear. what appears on the screen.
    key is what you can get from url.
    https://docs.google.com/spreadsheets/d/<<KEY>>/edit#gid=0
    :param type:
    :return:
    '''
    print "opening a sheet"
    if type == None or type in ["name", "n"]:
        print "open_a_spreadsheet: key type not specified. Assume it is name"
        wks = gc.open(key)
    elif type in ["key", "k"]:
        print "open_a_spreadsheet: received a key."
        wks = gc.open_by_key(key)
    elif type in ["url", "u"]:
        print "open_a_spreadsheet: received a url."
        wks = gc.open_by_url(key)
    else:
        print "open_a_spreadsheet: unknown error"
    return wks.sheet1



if __name__ == "__main__":
    authorize()