from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(2, 2)
qc.u(1.5707963267948966,0.0,-3.141592653589793,[0])
qc.u(0.92729522,0.0,0.0,[1])
qc.cx([0], [1])
qc.u(-0.92729522,0.0,1.0,[1])
qc.cx([0], [1])
qc.h([0])
qc.u(0.92729522,0.0,0.0,[1])
qc.barrier([0], [1])
