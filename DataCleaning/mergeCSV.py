import csv
import os
import tkinter as tk
from tkinter import filedialog

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    files = filedialog.askopenfilenames()
    lastProgram = ''
    first = True
    header = True
    for file in files:
        splited_file = file.split('/')
        splited_name = splited_file[-1].split('_')
        name = '_'.join(splited_name[0:-2])
        if first:
            first = False
            lastProgram = name
            path = '/'.join(splited_file[0:-1]) + '/mergedCsv/' + name + '.csv'
        else:
            if lastProgram != name:
                lastProgram = name
                path = '/'.join(splited_file[0:-1]) + '/mergedCsv/' + name + '.csv'
                header = True

        with open(path, 'a', newline='') as outfile:
            writer = csv.writer(outfile)
            with open(file, 'r') as infile:
                reader = csv.reader(infile)
                # Write each row from the current CSV file to the output file
                for row in reader:
                    if header:
                        header = False
                        writer.writerow(row)
                    else:
                        if row != ['Origin_program', 'Qubits', 'Operator', 'Gate', 'Position', 'Killed']:
                            writer.writerow(row)




