from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(2, 2)
qc.h([0])
qc.x([1])
qc.barrier([0], [1])
