# app.py
import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form.get("num1", "0"))
            num2 = float(request.form.get("num2", "0"))
            operation = request.form.get("operation", "add")

            if operation == "add":
                result = num1 + num2
            elif operation == "sub":
                result = num1 - num2
            elif operation == "mul":
                result = num1 * num2
            elif operation == "div":
                result = "Error: Divide by zero" if num2 == 0 else num1 / num2

        except ValueError:
            result = "Invalid input"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # debug=False for production; keep False in docker/k8s
    app.run(host="0.0.0.0", port=port, debug=False)

