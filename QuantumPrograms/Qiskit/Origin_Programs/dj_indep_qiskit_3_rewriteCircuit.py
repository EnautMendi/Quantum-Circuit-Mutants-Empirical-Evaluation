from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(3, 3)
qc.h([0])
qc.h([1])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[2])
qc.cx([0], [2])
qc.h([0])
qc.cx([1], [2])
qc.h([1])
qc.barrier([0], [1], [2])
