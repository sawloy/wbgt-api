from flask import Flask, jsonify
import pandas as pd
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/get_wbgt")
def get_wbgt():
    url = "https://www.wbgt.env.go.jp/graph_data/td_data_82056.csv"
    df = pd.read_csv(url, encoding='shift_jis')

    now_hour = datetime.now().strftime("%H:00")
    current_row = df[df["時刻"] == now_hour]
    if not current_row.empty:
        wbgt = current_row.iloc[0]["暑さ指数(WBGT)"]
        return jsonify({"wbgt": str(wbgt)})
    else:
        return jsonify({"wbgt": "N/A"})
