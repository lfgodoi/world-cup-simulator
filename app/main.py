from flask import Flask, render_template
import json
from sources.simulator import Simulator

with open("./app/config/groups.json", "rb") as file:
    groups = json.load(file)

app = Flask(__name__, template_folder="./sources/templates/pages")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run")
def run():
    simulator = Simulator(groups)
    simulator.run_group_stage()
    simulator.run_round_16()
    simulator.run_quarter_finals()
    simulator.run_semifinals()
    simulator.run_final()
    print(simulator.content_group_stage)
    print(simulator.content_knockout)
    return render_template("index.html", 
                           content_group_stage=simulator.content_group_stage,
                           content_knockout=simulator.content_knockout)

if __name__ == "__main__":
    app.run(debug=True)