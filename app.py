from flask import Flask

app = Flask(__name__)

@app.route("/get_wbgt")
def get_wbgt():
    return {"wbgt": "27"}
