import numpy as np

from qiskit import *

# method returns available real backends
def return_available_backends():
    provider = IBMQ.get_provider(hub='ibm-q');
    available_backends = provider.backends(filters=lambda x: x.configuration().n_qubits == 5
                                    and not x.configuration().simulator
                                    and x.status().operational==True)
    available_backends_names = []

    for val in available_backends:
        available_backends_names.append(val.name())
    return available_backends_names;


# method returns available real backends and simulators
def return_available_backends_and_simulator():
    provider = IBMQ.get_provider(hub='ibm-q');
    available_backends = provider.backends(filters=lambda x: x.configuration().n_qubits == 5
                                    and x.status().operational==True)
    available_backends_names = ["qasm_simulator"]

    for val in available_backends:
        available_backends_names.append(val.name())
    return available_backends_names;

def get_backend(name):
    if name == "qasm_simulator":
        simulator = Aer.get_backend('qasm_simulator')
        return simulator
    provider = IBMQ.get_provider(hub='ibm-q');
    backend = provider.get_backend(name)
    return backend


def get_backend_properties(backend_name):
    backend = get_backend(backend_name)
    properties = backend.properties(refresh=True)
    return properties.to_dict()
