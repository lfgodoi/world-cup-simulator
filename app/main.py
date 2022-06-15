# Importing packages and modules
from flask import (
    Flask, 
    render_template, 
    redirect,
    url_for, 
    session,
    request,
    jsonify
)
import json
from sources.simulator import Simulator

# Reading the file containing data from all groups
with open("./app/dao/groups.json", "rb") as file:
    groups = json.load(file)

# Reading the config file
with open("./app/dao/config.json", "rb") as file:
    config = json.load(file)

# Instantiating the app
app = Flask(__name__, template_folder="./templates", static_folder="static")
app.config['SECRET_KEY'] = 'mYkEy'
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Endpoint - Rendering the login page
@app.route("/login")
def login():
    return render_template("login.html")

# Endpoint - Authenticating the user
@app.route("/authenticate", methods=["POST",])
def authenticate():
    if request.form["username"] == config["username"] and request.form["password"] == config["password"]:
        session["active_user"] = request.form["username"]
        return redirect(url_for("index"))
    else:
        return redirect(url_for("login"))

# Endpoint - Rendering the main page
@app.route("/")
@app.route("/index")
def index():
    if "active_user" not in session or session["active_user"] == None:
        return render_template("login.html")
    else:
        return render_template("index.html")

# Endpoint - Running the simulation
@app.route("/run", methods=["POST",])
def run():
    simulator = Simulator(groups)
    simulator.run_group_stage()
    simulator.run_round_16()
    simulator.run_quarter_finals()
    simulator.run_semifinals()
    simulator.run_final()
    return jsonify({"content_group_stage" : simulator.content_group_stage, "content_knockout" : simulator.content_knockout})

# Running the app
if __name__ == "__main__":
    app.run(debug=True)