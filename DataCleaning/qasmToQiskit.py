import qiskit.circuit
from qiskit.circuit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.visualization import circuit_drawer
import tkinter as tk
from tkinter import filedialog
import math
import os


def circuitToFile(qc, file_path):
    splited_path = file_path.split('.')
    splited_path = splited_path[0].split('/')
    special_gates = ('u2','u3','u1','cu1')
    path = 'qasmToQiskitCircuits/' + splited_path[len(splited_path)-1] + '_rewriteCircuit.py'
    # Open the target Python script
    with open(path, 'w') as f:
        # Write imports
        f.write('from qiskit import QuantumCircuit, transpile\n')
        f.write('from qiskit_aer import AerSimulator\n')

        # Write the QuantumCircuit initialization
        f.write(f'qc = QuantumCircuit({qc.num_qubits}, {qc.num_qubits})\n')

        qubits_array = qc.qubits
        # Write the instructions
        for instruction, qubits, _ in qc.data:

            # Get the name of the instruction and the qubits it acts on
            instruction_name = instruction.name
            qubits = [qubits_array.index(qubit) for qubit in qubits]
            if len(qubits) > 1:
                strqubits = ""
                for qubit in qubits:
                    if qubit == int(qubits[len(qubits) - 1]):
                        strqubits = strqubits + "[" + str(qubit) + "]"
                    else:
                        strqubits = strqubits + "[" + str(qubit) + "], "
                qubits = strqubits
            if instruction_name in special_gates:
                if instruction_name == 'u3':
                    instruction_name = 'u'
                elif instruction_name == 'u2':
                    instruction_name = 'u'
                    instruction.params.insert(0, math.pi/2)
                elif instruction_name == 'u1':
                    instruction_name = 'p'
                elif instruction_name == 'cu1':
                    instruction_name = 'cu'
                    instruction.params.append(0)
                    instruction.params.append(0)
                    instruction.params.append(0)
            if instruction.params:
                param_names = []
                # If the instruction has parameters, write them as well
                for param in instruction.params:
                    if isinstance(param, Parameter):
                        # If the parameter is a Qiskit Parameter, write it as such
                        f.write(f'{param.name} = Parameter("{param.name}")\n')
                        param_names.append(param.name)
                    else:
                        # If the parameter is a simple type (e.g., int, float), write it directly
                        param_names.append(param)
                str_parameters = f'qc.{instruction_name}('
                for x in param_names:
                    str_parameters = str_parameters + str(x) + ','
                str_parameters = str_parameters + f'{qubits})\n'
                f.write(str_parameters)
            else:
                # If the instruction has no parameters, just write the instruction and the qubits
                if (instruction_name != "measure"):
                    f.write(f'qc.{instruction_name}({qubits})\n')
                #else:
                    # PASS, MEASUREMENT WILL BE INSERTED IN MUSKIT EXECUTION
                    # f.write(f'qc.{instruction_name}({qubits},{qubits})\n')




if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    files = filedialog.askopenfilenames()
    for file in files:

        qc = QuantumCircuit.from_qasm_file(file)
        circuitToFile(qc, file)