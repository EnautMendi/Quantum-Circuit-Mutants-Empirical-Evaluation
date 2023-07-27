from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(2, 2)
qc.h([0])
qc.x([1])
qc.cp(3.141592653589793,[1], [0])
qc.h([0])
qc.barrier([0], [1])
