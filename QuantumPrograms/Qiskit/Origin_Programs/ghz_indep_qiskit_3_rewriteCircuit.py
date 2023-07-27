from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(3, 3)
qc.h([2])
qc.cx([2], [1])
qc.cx([1], [0])
qc.barrier([0], [1], [2])
