import quantum_settings_service as qss
import quantum_circuit_creator as qcc
import num_to_binary_converter as nbc
import ibmq_quantum_service as iqs
from qiskit import *


def main():
    print("elo!")
    setup_quantum_connection()

    # backends = qss.return_available_backends_and_sim()
    # print(backends)

    backend = qss.get_backend("ibmq_quito")
    simulator = Aer.get_backend('qasm_simulator')
    iqs.run_program_on_backend(simulator)

    print("elo2")

def setup_quantum_connection():
    IBMQ.load_account()

# zrobić program
# program powinien rysować kwantowego sinusa

# będzie się podawało backend -> run
# moze liczbę powtórzeń
# będzie zwracało tablicę z wynikami
# moze po 5 obliczeń na raz, zeby było szybciej
# na dockerze zeby stało
# po stronie frontu - rusować normalną sinusoidę
main()