from flask import Flask, render_template, request, jsonify
from counter import get_transaction_count, calculate_risk_level  # Import functions

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        wallet_address = request.form.get("wallet")  # Get wallet input from form

        if not wallet_address:
            return jsonify({"error": "No wallet address provided"}), 400

        tx_count = get_transaction_count(wallet_address)
        if tx_count is None or tx_count == "Invalid wallet address":
            return jsonify({"error": "Invalid wallet address"}), 400

        risk_level = calculate_risk_level(tx_count)

        return jsonify({"wallet": wallet_address, "tx_count": tx_count, "risk_level": risk_level})

    return render_template("index.html")
application = app

if __name__ == "__main__":
    app.run(debug=True)
