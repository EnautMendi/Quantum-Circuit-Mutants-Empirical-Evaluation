from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(2, 2)
qc.u(2.6422546,-3.141592653589793,0.0,[0])
qc.u(1.3343007,-3.141592653589793,0.0,[1])
qc.cz([0], [1])
qc.ry(4.43809726294417,[0])
qc.ry(1.16893331500669,[1])
qc.barrier([0], [1])
