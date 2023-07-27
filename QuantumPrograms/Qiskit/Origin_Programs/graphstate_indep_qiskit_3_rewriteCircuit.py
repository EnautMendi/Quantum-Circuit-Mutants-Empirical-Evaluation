from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(3, 3)
qc.h([0])
qc.h([1])
qc.cz([0], [1])
qc.h([2])
qc.cz([0], [2])
qc.cz([1], [2])
qc.barrier([0], [1], [2])
