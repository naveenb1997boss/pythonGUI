from tkinter import *
from readCsv import *

def advanced():
    newWindow = Tk()

    OptionList = [
    "CAT1",
    "CAT2",
    "FAT"
    ] 

    readFile()
    variable = StringVar(newWindow)
    variable.set(OptionList[0])

    Label(newWindow, text='Find').grid(row=0, column=0)

    OptionMenu(newWindow, variable, *OptionList).grid(row=1, column=0)


    resultEntry = Entry(newWindow)
    resultEntry.grid(row=100,column=0)
    Button(newWindow, text="Maximum", command=lambda : findMax(variable.get(), resultEntry)).grid(row=2, column=2)
    Button(newWindow, text="Minimum", command=lambda : findMin(variable.get(), resultEntry)).grid(row=2, column=3)
    Button(newWindow, text="Mean", command=lambda : findMean(variable.get(), resultEntry)).grid(row=3, column=2)
    Button(newWindow, text="Median", command=lambda : findMedian(variable.get(), resultEntry)).grid(row=3, column=3)
    Button(newWindow, text="Variance", command=lambda : findVariance(variable.get(), resultEntry)).grid(row=4, column=2)
    Button(newWindow, text="Standard Deviation", command=lambda : findStandardDeviation(variable.get(), resultEntry)).grid(row=4, column=3)

    newWindow.mainloop()