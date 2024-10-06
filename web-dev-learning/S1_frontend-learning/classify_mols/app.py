from flask import Flask, render_template, jsonify

app = Flask(__name__)


# Route to serve the webpage
@app.route("/")
def index():
    # Python data structure mimicking data from a MySQL query
    molecules = [
        {"name": "Aspirin", "smiles": "CC(=O)OC1=CC=CC=C1C(=O)O"},
        {"name": "Diethyl ether", "smiles": "CCOCC"},
        {"name": "Acetamide", "smiles": "CC(=O)N"},
        {
            "name": "Triphenyl phosphate",
            "smiles": "C1=CC=C(C=C1)P(=O)(OC2=CC=CC=C2)OC3=CC=CC=C3",
        },
        {"name": "Pyridine", "smiles": "C1=CC=NC=C1"},
    ]
    return render_template("index.html", molecules=molecules)


if __name__ == "__main__":
    app.run(debug=True)
