# Imports ------------------------------
import tkinter as tk
import csv
main = tk.Tk()

assesmentObj = {
    'student': {
        'rowNumber': 1,
        'name': tk.Entry(main),
        'number': tk.Entry(main)
    },
    'cat1': {
        'rowNumber': 3,
        'mark': tk.Entry(main),
        'grade': tk.Entry(main)
        },
    'cat2': {
        'rowNumber': 4,
        'mark': tk.Entry(main),
        'grade': tk.Entry(main)
        },
    'cat3': {
        'rowNumber': 5,
        'mark': tk.Entry(main),
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
        else:
            columnNumber = 0
            showLabel(key+' Mark', row, columnNumber, assessment['mark'])
            columnNumber += 3
            showLabel(key+' Grade', row, columnNumber, assessment['grade'])
    
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
        else:
            insertingRow.append(assessment['mark'].get())
            assessment['mark'].delete(0, 'end')
            insertingRow.append((assessment['grade'].get()).upper())
            assessment['grade'].delete(0, 'end')
    return insertingRow

def store_in_csv():
    with open('dina.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(insert_row_generaor())

# Main concept -----------------------
main.title('Calculator')
entryFieldsInit()
tk.Button(main, text="Store to CSV", command=store_in_csv).grid(row=100, column=3)
main.mainloop()
