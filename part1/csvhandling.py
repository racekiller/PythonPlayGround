# This program should take all non numeric values and convert them
# to null

import csv
import sys

# def CSVDataGathering():
with open('CSVExample.csv',newline='') as csvfile:
	SensorData = csv.reader(csvfile, delimiter=',')
	for row in SensorData:
		print(', '.join(row))

# def CSVNonNumericReplace(fileName):


# def main():
# 	print("This is the main module")
# 	CSVDataGathering()


# # main method
# if __name__ == '__main__':
#     main()