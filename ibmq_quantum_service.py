import quantum_settings_service as qss
import quantum_circuit_creator as qcc
import num_to_binary_converter as nbc
import num_to_angle_converter as nta
from collections import OrderedDict

from qiskit import *

# function responsible for running all circuits on selected backend
def run_program_on_backend(backend, num_of_shots):
    # Dividing circuits to batches optimizes time needed to run them.
    # IBMQ program allows for running 5 circuits simultaneously
    circuits_to_run = []
    for i in range (16):
        configuration = nbc.convert(i)
        circuit = qcc.create_quantum_cosine_circuit(configuration)
        transpiled = transpile(circuit, backend)
        circuits_to_run.append(transpiled)
        print("Transpiled circuit " + str(i))

    return run_experiment(circuits_to_run, backend, num_of_shots)


# Function responsible for running batch of 4 quantum circuits simultaneously on selected backend
def run_experiment(circuits_to_run, backend, num_of_shots):
    print("Running " + str(len(circuits_to_run)) + " circuits (hopefully)")
    job = backend.run(circuits_to_run, shots=num_of_shots);

    counts = job.result().get_counts();
    results = OrderedDict()
    keyorder = nta.get_angles()
    for i in range (16):
        res = counts[i].get('00000', 0);
        angle = nta.convert(i)
        results[angle] = res

    return OrderedDict(sorted(results.items(), key=lambda i:keyorder.index(i[0])))
