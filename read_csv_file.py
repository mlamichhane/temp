import csv
import statistics

temperature = []                                        # create an empty list

with open('paripatle2.csv') as csv_file:                # open a file
    file_data = csv.reader(csv_file, delimiter=",")     # read file data
    line_number = 0                                     # row number starts with 0
    for row in file_data:                               # Looping each row
        if line_number > 0 and row[3] != 'nan':         # read the temperature value (the 4th column) omitting 'nan' values
            temperature.append(float(row[3]))           # add the temperatue value to the list   
        line_number += 1                                # move to the next row


print("Total valid records  : ", len(temperature))      # Total records without 'nan' values
print("Minimium Temperature : " , min(temperature))     # Minimun temperature value
print("Maximum Temperature  : " , max(temperature))     # Maximum temperature value

# for mean and median we need to use statistics module from Python library
print("Mean of Temperature  : {0:.2f}" .format(statistics.mean(temperature)))
print("Median of Temperature: ", statistics.median(temperature))

