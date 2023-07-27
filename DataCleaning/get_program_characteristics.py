import math
import qiskit
from qiskit.circuit import QuantumCircuit
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import rustworkx
import QuantumGates
def checkEntanglement(qc):
    entangled_qubits = 0
    h_qubit = None
    h_gates = 0
    counted_qubits = []
    for instruction, qubits, _ in qc.data:
        if instruction.name == 'h':
            h_gates = h_gates + 1

    for x in range(h_gates):
        h = False
        cx = False
        h_number = 0
        for instruction, qubits, _ in qc.data:
            if instruction.name == 'h':
                if h == False and h_number == x:
                    h = True
                    h_qubit = qubits[0]
                h_number = h_number + 1
            if instruction.name == 'cx' and h == True:
                if qubits[0] == h_qubit:
                    for qubit in qubits:
                        if qubit not in counted_qubits:
                            counted_qubits.append(qubit)
                            entangled_qubits = entangled_qubits + 1
                    cx = True
                if qubits[0] in counted_qubits and cx == True:
                    for qubit in qubits:
                        if qubit not in counted_qubits:
                            counted_qubits.append(qubit)
                            entangled_qubits = entangled_qubits + 1

    return entangled_qubits


def getCharacteristics(qc, file_name):
    splited_name = file_name.split('_')
    splited_name = splited_name[0:-1]
    group = ''.join(splited_name)
    characteristics = []
    measurement_gates = 0
    num_gates = 0
    singlequbit_gates = 0
    multiqubit_gates = 0
    entangled_qubits = checkEntanglement(qc)
    for instruction, qubits, _ in qc.data:
        if instruction.name != 'measure':
            num_gates = num_gates + 1
            if instruction.name in QuantumGates.OneQubit:
                singlequbit_gates = singlequbit_gates + 1
            else:
                multiqubit_gates = multiqubit_gates + 1
        else:
            measurement_gates = measurement_gates + 1
    characteristics.append(group)
    characteristics.append(qc.num_qubits)
    characteristics.append(num_gates)
    characteristics.append(measurement_gates)
    characteristics.append(qc.depth())
    characteristics.append(singlequbit_gates)
    characteristics.append(multiqubit_gates)
    characteristics.append(entangled_qubits)
    return characteristics


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    files = filedialog.askopenfilenames()
    df_new = pd.DataFrame(columns=['group', 'qubits', 'gates', 'measurement_gates', 'depth', 'singlequbit_gates', 'multiqubit_gates', 'entangled_qubits'])
    for file in files:
        qc = QuantumCircuit.from_qasm_file(file)
        splited = file.split('/')
        file_name = splited[-1]
        df_new.loc[file_name] = getCharacteristics(qc, file_name)
    df_new.to_excel('programs_characteristics.xlsx', sheet_name='characteristics')
