import tkinter as tk
from tkinter import filedialog

def merge_files(files):
    with open('mergedMutants.txt', 'a') as merged_file:
        for file in files:
            with open(file, 'r') as fp:
                for line in fp:
                    if "The result of" in line:
                        merged_file.write(line)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    files = filedialog.askopenfilenames()
    merge_files(files)