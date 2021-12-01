from flask import Flask, jsonify
from flask import render_template, request, redirect, url_for, flash
import time

app = Flask("Projekt Domański")

@app.route('/', methods=['GET'])
def index():
    return 0


@app.route('/api/run_quantum_program', methods=['POST'])
def run_quantum_program():
    request_body = request.get_json()
    backend_name = request_body["backend_name"]
    num_of_shots = request_body["num_of_shots"]
    program = request_body["program"]
    time.sleep(20)
    data = {"backend_name": backend_name, "num_of_shots": num_of_shots, "program": program}
    return jsonify(data), 200


app.secret_key = 'super secret key'
app.config.from_object(__name__)
app.debug = True
app.run()