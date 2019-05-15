import csv

with open('object_counting_report.csv' ,'r') as reading:
            read = csv.reader(reading)
            for line in read:
                for l in line:
                    name = []
                    number = []
                    for item in l:
                        if item.isalpha():
                            name.append(item)
                        elif item.isdigit():
                            number.append(int(item))
                        else:
                            pass
                    name = (''.join(c for c in name) )
                    number= (number[0])