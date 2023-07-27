from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(7, 7)
qc.h([6])
qc.cx([6], [5])
qc.cx([5], [4])
qc.cx([4], [3])
qc.cx([3], [2])
qc.cx([2], [1])
qc.cx([1], [0])
qc.barrier([0], [1], [2], [3], [4], [5], [6])
