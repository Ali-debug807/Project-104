import csv

with open('data.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop()
def mean(totalWeight,totalEntries):
    mean = totalWeight/totalEntries
    print(mean)
def median(totalEntries,sortedData):
    median1 = float(sortedData[totalEntries//2])
    median2 = float(sortedData[totalEntries//2-1])
    median = median1+median2/1
    print(median)
mean()
median()