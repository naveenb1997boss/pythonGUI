import csv
import numpy as np
from tkinter import *
import matplotlib.pyplot as plt 

readCsvObject = {
    'CAT1': [],
    'CAT2': [],
    'FAT': [],
    'grade': []
}

def readFile():
    with open('dina.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            readCsvObject['CAT1'].append(int(row[2]))
            readCsvObject['CAT2'].append(int(row[3]))
            readCsvObject['FAT'].append(int(row[4]))
            readCsvObject['grade'].append(row[6])

    print(readCsvObject)
    print(np.mean(readCsvObject['CAT1']))

def clearValue(windowObj):
    windowObj.delete(0, 'end')

def findMean(markArrayName, windowObj):
    clearValue(windowObj)
    windowObj.insert(0, np.mean(readCsvObject.get(markArrayName)))
    print('inside mean')

def findMedian(markArrayName, windowObj):
    clearValue(windowObj)
    windowObj.insert(0, np.median(readCsvObject.get(markArrayName)))

def findMax(markArrayName, windowObj):
    clearValue(windowObj)
    windowObj.insert(0, str(max(readCsvObject.get(markArrayName))))

def findMin(markArrayName, windowObj):
    clearValue(windowObj)
    windowObj.insert(0, str(min(readCsvObject.get(markArrayName))))

def findStandardDeviation(markArrayName, windowObj):
    clearValue(windowObj)
    windowObj.insert(0, np.std(readCsvObject.get(markArrayName)))

def findVariance(markArrayName, windowObj):
    clearValue(windowObj)
    windowObj.insert(0, np.var(readCsvObject.get(markArrayName)))

def findCorrelation(markArrayName1, markArrayName2, windowObj):
    clearValue(windowObj)
    windowObj.insert(0, np.correlate(readCsvObject[markArrayName1], readCsvObject[markArrayName2])[0])

def plotHistogram():
    plt.hist(readCsvObject['grade'], bins=10, range=(0, 100), color = 'green', 
        histtype = 'bar', rwidth = 0.8)
    plt.xlabel('Grades')
    plt.ylabel('No. of stidents')
    plt.title('Student Grade histogram')
    plt.show()
