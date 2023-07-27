import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import json
import pandas as pd
from scipy.stats import chisquare

import QuantumGates
import mergeFiles


def getOriginInfo(line):
    splited_line = line.split(' is: ')

    split = splited_line[0].split('/')
    split1 = split[-1].split("_rewriteCircuit.py")
    name = split1[0]

    name_split = name.split("_")
    qubits = int(name_split[-1])

    splited_line[1] = splited_line[1].replace(chr(39), chr(34))
    output = json.loads(splited_line[1])
    return name,qubits,output


def getGateForPosition(origin_name, position):
    splitChar = 92
    folder_path = r'C:\Users\Enaut\Desktop\Enaut\PhD\Experiments\Final_experiments_ICSE\SelectedPrograms\Qiskit\Origin_Programs'
    origin_path = folder_path + chr(splitChar) + origin_name + '_rewriteCircuit.py'
    x = 1
    f = open(origin_path)
    line = f.readline()
    while x <= position:
        if ('qc' in line) and ("QuantumCircuit" not in line):
            temp = line.split(".", 1)
            temp2 = temp[1].split("(")
            if temp2[0] in QuantumGates.AllGates:
                x = x + 1
                gate = temp2[0]
        line = f.readline()

    return gate


def getMutantsInfo(line):
    splited_line = line.split(' is: ')

    split = splited_line[0].split('/')
    split1 = split[-2].split("_rewriteCircuit")
    split1 = split1[0].split("Mutants_")
    origin_name = split1[1]

    split2 = split[-1].split("_rewriteCircuit.py")
    name = split2[0]

    name = name.replace("_.py", ".py")
    name_split = name.split("_")
    operator = name_split[0].split("Gate")
    operator = operator[0]

    position = name_split[-1].split(".py")
    position = position[0]

    if operator == "Remove":
        gate = getGateForPosition(origin_name, int(position))
    else:
        gate = name_split[1]

    splited_line[1] = splited_line[1].replace(chr(39), chr(34))
    output = json.loads(splited_line[1])

    return origin_name, name, operator, gate, position, output

def compareOutputs(expected, observed):
    sorted_expected = dict(sorted(expected.items()))
    sorted_observed = dict(sorted(observed.items()))
    if len(list(sorted_observed.values())) == len(list(sorted_expected.values())):
        if sorted_expected.keys() == sorted_observed.keys():
            result = chisquare(list(sorted_observed.values()), list(sorted_expected.values()))
            if result[1] > 0.01:
                killed = 'Survivor'
            else:
                killed = 'OPO'
        else:
            killed = 'WOO'
    else:
        killed = 'WOO'

    return killed


def evaluateMutants(df_origin, df_mutants):
    df_results = pd.DataFrame(columns=["Origin_program", "Qubits", "Operator", "Gate", "Position", "Killed"])
    df_results['Killed'] = df_results['Killed']

    for index, row in df_mutants.iterrows():
        origin_values = df_origin.loc[df_origin["Name"] == row["Origin"]]
        result = compareOutputs(json.loads(origin_values.iloc[0]["Output"]), json.loads(row["Output"]))
        new_row = {"Origin_program": row["Origin"], "Qubits": origin_values.iloc[0]["Qubits"], "Operator": row["Operator"],
                             "Gate": row["Gate"], "Position": row["Position"], "Killed": result}
        df_row = pd.DataFrame(new_row, index=[0])
        df_row['Killed'] = df_row['Killed']
        df_results = pd.concat([df_results, df_row], ignore_index=True)

    return df_results

def start(origin_file, mutants_file):

    df_origin = pd.DataFrame(columns=["Name","Qubits","Output"])

    with open(origin_file, 'r') as fp:
        for line in fp:
            if "The result of" in line:
                origin_info = getOriginInfo(line)
                origin_info_dict = {"Name": origin_info[0], "Qubits": origin_info[1], "Output": json.dumps(origin_info[2])}
                df_info = pd.DataFrame(origin_info_dict, index = [0])
                df_origin=pd.concat([df_origin, df_info], ignore_index=True)

    df_mutants = pd.DataFrame(columns=["Origin", "Name", "Operator", "Gate", "Position", "Output"])
    first = True
    last_origin = None

    with open(mutants_file, 'r') as fp:
        for line in fp:
            if "The result of" in line:

                mutants_info = getMutantsInfo(line)
                if first == True:
                    first = False
                    last_origin = mutants_info[0]
                else:
                    if last_origin != mutants_info[0]:
                        df_results = evaluateMutants(df_origin, df_mutants)
                        path = 'resultsCsv/' + last_origin + '_results.csv'
                        df_results.to_csv(path, index=False)
                        df_mutants = df_mutants[0:0]
                        last_origin = mutants_info[0]

                mutants_info_dict = {"Origin": mutants_info[0], "Name": mutants_info[1], "Operator": mutants_info[2], "Gate": mutants_info[3], "Position": mutants_info[4], "Output": json.dumps(mutants_info[5])}
                df_info = pd.DataFrame(mutants_info_dict, index=[0])
                df_mutants = pd.concat([df_mutants, df_info], ignore_index=True)

        df_results = evaluateMutants(df_origin, df_mutants)
        path = 'resultsCsv/' + last_origin + '_results.csv'
        df_results.to_csv(path, index=False)
        df_mutants = df_mutants[0:0]
        last_origin = mutants_info[0]

if __name__ == "__main__":
    origin_file = r"C:\Users\Enaut\Desktop\Enaut\PhD\Experiments\Final_experiments_ICSE\SelectedPrograms\Qiskit\Execution_ouputs\Oracle_origin\mergedOrigin.txt"
    mutants_file = r"C:\Users\Enaut\Desktop\Enaut\PhD\Experiments\Final_experiments_ICSE\SelectedPrograms\Qiskit\Execution_ouputs\Mutants_executions\mergedMutants.txt"
    start(origin_file, mutants_file)
