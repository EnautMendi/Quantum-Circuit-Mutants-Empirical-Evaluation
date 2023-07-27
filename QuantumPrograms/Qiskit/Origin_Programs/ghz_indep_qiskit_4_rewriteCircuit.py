from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(4, 4)
qc.h([3])
qc.cx([3], [2])
qc.cx([2], [1])
qc.cx([1], [0])
qc.barrier([0], [1], [2], [3])
