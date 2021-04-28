"""
this class is for handling all car output files so i can graph them 
"""

import csv


def writeFiles(name,item,datafine,dataGeneral):

    with open(str(name)+'.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        
        employee_writer.writerow(['item', 'data_general', 'data_finer'])
        employee_writer.writerow([item, datafine, dataGeneral])
        employee_file.flush()
        
