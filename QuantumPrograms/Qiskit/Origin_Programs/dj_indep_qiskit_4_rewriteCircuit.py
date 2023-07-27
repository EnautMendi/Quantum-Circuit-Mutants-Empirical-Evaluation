from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(4, 4)
qc.h([0])
qc.h([1])
qc.h([2])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[3])
qc.cx([0], [3])
qc.h([0])
qc.cx([1], [3])
qc.h([1])
qc.cx([2], [3])
qc.h([2])
qc.barrier([0], [1], [2], [3])
