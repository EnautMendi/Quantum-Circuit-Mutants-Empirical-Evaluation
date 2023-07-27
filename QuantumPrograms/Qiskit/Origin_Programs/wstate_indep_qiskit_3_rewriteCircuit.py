from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(3, 3)
qc.ry(-0.7853981633974483,[0])
qc.ry(-0.95531662,[1])
qc.x([2])
qc.cz([2], [1])
qc.ry(0.95531662,[1])
qc.cz([1], [0])
qc.ry(0.7853981633974483,[0])
qc.cx([1], [2])
qc.cx([0], [1])
qc.barrier([0], [1], [2])
