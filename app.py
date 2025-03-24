from flask import Flask, render_template, request, redirect, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_expense():
    amount = request.form.get("amount")
    category = request.form.get("category")
    date = request.form.get("date")
    description = request.form.get("description")
    
    new_expense = {
        "amount": float(amount),
        "category": category,
        "date": date,
        "description": description
    }
    
    expenses = load_expenses()
    expenses.append(new_expense)
    save_expenses(expenses)
    
    return redirect("/expenses")

@app.route("/expenses")
def expenses():
    expenses = load_expenses()
    total_expense = sum(exp["amount"] for exp in expenses)
    return render_template("expenses.html", expenses=expenses, total=total_expense)

if __name__ == "__main__":
    app.run(debug=True)
