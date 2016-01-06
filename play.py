from auth import authorize
from auth import open_a_spreadsheet
global gc
gc, wks = authorize()

wks.update_acell('B2', "Example")

def insert_data_by_row(start_point, list_of_dict, sheet_key = None, key_type = None):
    '''

    :param start_point: tuple of start point. If start from A1, then (1, 1)
    :param list_of_dict:
    :param sheet_key:
    :param key_type:
    :return:
    '''
    if sheet_key == None:
        wks = open_a_spreadsheet(gc,
                                 key = "1NqMxXEBGH9VR-Y8fqJFHfMdOwSHHBjHj6oPSyPOuqGA",
                                 type = "k")
    else:
        wks = open_a_spreadsheet(gc, key = sheet_key, type = key_type)

    sheet_x = start_point[0]
    sheet_y = start_point[1]

    for i in range(len(list(list_of_dict))):
        datum = str(list(list_of_dict)[i])
        wks.update_cell(sheet_x, sheet_y, datum)
        print ("wrote", sheet_x, sheet_y, datum)
        sheet_y += 1

start_point = (1,1)
list_of_dict = {"1":"v1", "2":"v2", "3":"v3", "4":"v3", "5":"v3", "6":"v3","7":"v3","8":"v3"}
sheet_key = "https://docs.google.com/spreadsheets/d/1NqMxXEBGH9VR-Y8fqJFHfMdOwSHHBjHj6oPSyPOuqGA/edit#gid=0"
key_type = "url"

insert_data_by_row(start_point, list_of_dict, sheet_key, key_type)
