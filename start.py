# Imports ------------------------------
import tkinter as tk
import csv
from numpyFunctionality import *
main = tk.Tk()

assesmentObj = {
    'student': {
        'rowNumber': 1,
        'name': tk.Entry(main),
        'number': tk.Entry(main)
    },
    'cat1': {
        'rowNumber': 3,
        'mark': tk.Entry(main)
        },
    'cat2': {
        'rowNumber': 4,
        'mark': tk.Entry(main)
        },
    'fat': {
        'rowNumber': 5,
        'mark': tk.Entry(main)
        },
    'total': {
        'rowNumber': 6,
        'mark': tk.Entry(main)
        },
    'grade': {
        'rowNumber': 7,
        'grade': tk.Entry(main)
    }
}

# Function concept -----------------------
def entryFieldsInit():
    for key,assessment in assesmentObj.items():
        row = assessment['rowNumber']
        if(key == 'student'):
            showLabel('Name', row, 0, assessment['name'])
            showLabel('Reg. Number', row+1, 0, assessment['number'])
        elif(key == 'grade'):
            showLabel('Grade', row, 0, assessment['grade'])
        else:
            columnNumber = 0
            showLabel(key+' Mark', row, columnNumber, assessment['mark'])
    
def showLabel(labelText, rowNumber, columnNumber, variable):
    tk.Label(main, text=labelText).grid(row=rowNumber, column=columnNumber)
    variable.grid(row=rowNumber, column=columnNumber+1)

def insert_row_generaor():
    insertingRow = []
    for key,assessment in assesmentObj.items():
        if(key == 'student'):
            insertingRow.append(assessment['name'].get())
            assessment['name'].delete(0, 'end')
            insertingRow.append(assessment['number'].get())
            assessment['number'].delete(0, 'end')
        elif(key == 'grade'):
            insertingRow.append(assessment['grade'].get())
            assessment['grade'].delete(0, 'end')
        else:
            insertingRow.append(assessment['mark'].get())
            assessment['mark'].delete(0, 'end')
    return insertingRow

def store_in_csv():
    with open('dina.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(insert_row_generaor())

def calculate_total_mark_grade():
    totalMark = 0
    for key,assessment in assesmentObj.items():
        if(key == 'cat1'):
            attained_mark = float(assessment['mark'].get())
            totalMark +=(attained_mark * (3/500))
        elif(key == 'cat2'):
            attained_mark = float(assessment['mark'].get())
            totalMark +=(attained_mark * (3/500))
        elif (key == 'fat'):
            attained_mark = float(assessment['mark'].get())
            totalMark +=(attained_mark * (2/500))
    assesmentObj['total']['mark'].delete(0, 'end')
    assesmentObj['total']['mark'].insert(0, totalMark*100)
    stdMark = totalMark*100
    grade=''
    if stdMark <= 100 and stdMark > 90:
        grade = 'S'
    elif stdMark <= 90 and stdMark > 80:
        grade = 'A'
    elif stdMark <= 80 and stdMark > 70:
        grade = 'B'
    elif stdMark <= 70 and stdMark > 60:
        grade = 'C'
    elif stdMark <= 60 and stdMark > 50:
        grade = 'D'
    elif stdMark <= 50 and stdMark >= 45:
        grade = 'E'
    else:
        grade = 'N'
    assesmentObj['grade']['grade'].delete(0, 'end')
    assesmentObj['grade']['grade'].insert(0, grade)
        
# Main concept -----------------------
main.title('Grade Calculator')
entryFieldsInit()
tk.Button(main, text="Calculate", command=calculate_total_mark_grade).grid(row=99,column=3)
tk.Button(main, text="Store to CSV", command=store_in_csv).grid(row=100, column=3)
tk.Button(main, text="Advanced", command=advanced).grid(row=101, column=3)
main.mainloop()

