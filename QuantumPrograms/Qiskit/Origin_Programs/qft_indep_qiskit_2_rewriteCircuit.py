from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(2, 2)
qc.h([1])
qc.cp(1.5707963267948966,[1], [0])
qc.h([0])
qc.swap([0], [1])
qc.barrier([0], [1])
