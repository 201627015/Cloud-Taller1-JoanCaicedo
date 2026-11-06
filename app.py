import os
from flask import Flask, request
from datetime import datetime, date
import read_value_yf

app = Flask(__name__)


@app.route("/")
def hello_world():
    # Filtros: ticker (nombre de la accion), sd (fecha inicial), ed (fecha final)
    ticker = request.args.get("ticker", "GOOGL")
    sd = request.args.get("sd", "2020-01-01")
    ed = request.args.get("ed", date.today().isoformat())
    data = read_value_yf.get_stock_data(sd, ticker, ed)
    return (
        f"<h1>Stock: {ticker}</h1>"
        f"<p>Rango: {sd} → {ed}</p>"
        f"{data.to_html()}"
    )


if __name__ == "__main__":
    # En macOS el puerto 5000 suele estar ocupado por AirPlay Receiver.
    # Local: PORT=5001 python3 app.py
    # Docker/AWS: usa 5000 por defecto (como en la guia).
    print(f"{datetime.now()}")
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
