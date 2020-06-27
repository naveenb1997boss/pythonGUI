from tkinter import *
from readCsv import *

def advanced():
    newWindow = Tk()
    newWindow.title('Advanced Settings')

    OptionList = [
    "CAT1",
    "CAT2",
    "FAT"
    ] 

    readFile()
    variable = StringVar(newWindow)
    variable.set(OptionList[0])
    correlationVar1 = StringVar(newWindow)
    correlationVar2 = StringVar(newWindow)
    correlationVar1.set(OptionList[0])
    correlationVar2.set(OptionList[0])

    Label(newWindow, text='Find').grid(row=0, column=0)

    OptionMenu(newWindow, variable, *OptionList).grid(row=1, column=0)


    resultEntry = Entry(newWindow)
    resultEntry.grid(row=100,column=5)
    Button(newWindow, text="Maximum", command=lambda : findMax(variable.get(), resultEntry)).grid(row=2, column=2)
    Button(newWindow, text="Minimum", command=lambda : findMin(variable.get(), resultEntry)).grid(row=2, column=3)
    Button(newWindow, text="Mean", command=lambda : findMean(variable.get(), resultEntry)).grid(row=3, column=2)
    Button(newWindow, text="Median", command=lambda : findMedian(variable.get(), resultEntry)).grid(row=3, column=3)
    Button(newWindow, text="Variance", command=lambda : findVariance(variable.get(), resultEntry)).grid(row=4, column=2)
    Button(newWindow, text="Standard Deviation", command=lambda : findStandardDeviation(variable.get(), resultEntry)).grid(row=4, column=3)

    Label(newWindow, text="Correlation between").grid(row=5, column=1)
    OptionMenu(newWindow, correlationVar1, *OptionList).grid(row=5, column=2)
    Label(newWindow, text="and").grid(row=5, column=3)
    OptionMenu(newWindow, correlationVar2, *OptionList).grid(row=5, column=4)
    Button(newWindow, text="Correlation", command=lambda: findCorrelation(correlationVar1.get(), correlationVar2.get(), resultEntry)).grid(row=5, column=5)
    Button(newWindow, text="Plot Histogram", command=plotHistogram).grid(row=6, column=3)

    newWindow.mainloop()
