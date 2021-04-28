"""
this class is for handling all car output files so i can graph them 
"""

def writeFiles():

    with open('employee_file.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        employee_writer.writerow(['John Smith', 'Accounting', 'November'])
        employee_writer.writerow(['Erica Meyers', 'IT', 'March'])