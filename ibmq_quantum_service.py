import quantum_settings_service as qss
import quantum_circuit_creator as qcc
import num_to_binary_converter as nbc

from qiskit import *

# function responsible for running all circuits on selected backend
def run_program_on_backend(backend):
    # Dividing circuits to batches optimizes time needed to run them.
    # IBMQ program allows for running 5 circuits simultaneously
    circuits_to_run = []
    for i in range (16):
        configuration = nbc.convert(i)
        circuit = qcc.create_quantum_cosine_circuit(configuration)
        transpiled = transpile(circuit, backend)
        circuits_to_run.append(transpiled)
        print("Transpiled circuit " + str(i))

    run_experiment(circuits_to_run, backend)


# Function responsible for running batch of 4 quantum circuits simultaneously on selected backend
def run_experiment(circuits_to_run, backend):
    print("Running " + str(len(circuits_to_run)) + " circuits (hopefully)")
    job = backend.run(circuits_to_run);

    result = job.result().get_counts();
    print(result)
    print("Done")