from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(3, 3)
qc.u(2.7702916,-3.141592653589793,0.0,[0])
qc.u(0.26055497,0.0,-3.141592653589793,[1])
qc.cz([0], [1])
qc.u(3.0295952,-3.141592653589793,0.0,[2])
qc.cz([0], [2])
qc.ry(1.85578983194329,[0])
qc.cz([1], [2])
qc.ry(4.54167162188708,[1])
qc.ry(2.28793740781859,[2])
qc.barrier([0], [1], [2])
