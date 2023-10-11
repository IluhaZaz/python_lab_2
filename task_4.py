import csv

def get_next(class_mark:str,reader:csv.reader)->str:
    """Function returns next string in csv file opened in 'reader'"""
    for row in reader:
        if row[2] == class_mark:
            return row[0]
    return None



