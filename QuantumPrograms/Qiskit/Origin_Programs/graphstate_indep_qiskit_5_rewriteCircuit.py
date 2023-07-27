from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(5, 5)
qc.h([0])
qc.h([1])
qc.cz([0], [1])
qc.h([2])
qc.h([3])
qc.cz([1], [3])
qc.cz([2], [3])
qc.h([4])
qc.cz([0], [4])
qc.cz([2], [4])
qc.barrier([0], [1], [2], [3], [4])
