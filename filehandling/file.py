import csv
with open('data.csv', mode ='r') as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        print(lines)


with open('data.txt') as data:
    print(data.read()) # reads the whole file
    print(data.readline()) # reads a single line
    print(data.readlines()) # reads all lines
