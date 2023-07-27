from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(2, 2)
qc.ry(-0.7853981633974483,[0])
qc.x([1])
qc.cz([1], [0])
qc.ry(0.7853981633974483,[0])
qc.cx([0], [1])
qc.barrier([0], [1])
