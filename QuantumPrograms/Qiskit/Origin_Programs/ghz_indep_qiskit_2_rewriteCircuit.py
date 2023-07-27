from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(2, 2)
qc.h([1])
qc.cx([1], [0])
qc.barrier([0], [1])
