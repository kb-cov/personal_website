from flask import Flask, render_template

from get_crypto_prices import endpoint_list, get_crypto_data

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/crypto")
def crypto():
    crypto_data = get_crypto_data(endpoint_list)
    return render_template("crypto.html", crypto_data=crypto_data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
