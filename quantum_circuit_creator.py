from qiskit import *
import math

# creating circuit 1/2(1+cos(phi))
def create_quantum_cosine_circuit(configuration):
    
    # creating 5 qubit quantum register
    qr = QuantumRegister(5)
    cr = ClassicalRegister(5)
    circuit = QuantumCircuit(qr, cr)
    
    # resetting all qubits to 0
    circuit.reset(qr[0])
    circuit.reset(qr[1])
    circuit.reset(qr[2])
    circuit.reset(qr[3])
    circuit.reset(qr[4])

    # applying h gate to ancillae qubit
    circuit.h(qr[4])
    
    # applying negations to certain qubits
    for i in range(4):
        if len(configuration) > i and configuration[i] == 1:
            circuit.x(qr[i])
    
    # applying phase shift gates to qubits
    circuit.p(-math.pi, qr[4])
    circuit.cp(math.pi, qr[4], qr[0])
    circuit.cp(math.pi/2,  qr[4], qr[1])
    circuit.cp(math.pi/4, qr[4], qr[2])
    circuit.cp(math.pi/8, qr[4], qr[3])

    # applying second H gate co ancillae qubit, and measuring it
    circuit.h(qr[4])
    circuit.measure(qr[4], cr[4])
    
    return circuit