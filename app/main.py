from flask import Flask
import json
from sources.simulator import Simulator

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route("/run")
def run():
    with open("config/groups.json", "rb") as file:
        groups = json.load(file)
    simulator = Simulator(groups)
    simulator.run_group_stage()
    simulator.run_round_16()
    simulator.run_quarter_finals()
    simulator.run_semifinals()
    simulator.run_final()

    return "haha"

if __name__ == "__main__":
    app.run(debug=True)