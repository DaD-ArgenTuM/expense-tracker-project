from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"
CATEGORIES = ["Food", "Transport", "Bills", "Shopping", "Health", "Entertainment", "Education", "Travel", "Savings", "Other"]

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
    return render_template("index.html", categories=CATEGORIES)

@app.route("/add", methods=["POST"])
def add_expense():
    amount = request.form.get("amount")
    category = request.form.get("category")
    date = request.form.get("date")
    description = request.form.get("description")
    
    new_expense = {
        "id": os.urandom(8).hex(),
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

    selected_category = request.args.get("category")
    if selected_category and selected_category != "All":
        expenses = [exp for exp in expenses if exp["category"] == selected_category]

    return render_template("expenses.html", expenses=expenses, total=total_expense, categories=CATEGORIES, selected_category=selected_category)

@app.route("/delete/<expense_id>", methods=["POST"])
def delete_expense(expense_id):
    expenses = load_expenses()
    expenses = [exp for exp in expenses if exp["id"] != expense_id]
    save_expenses(expenses)
    return redirect("/expenses")

@app.route("/edit/<expense_id>", methods=["GET", "POST"])
def edit_expense(expense_id):
    expenses = load_expenses()
    
    if request.method == "POST":
        for exp in expenses:
            if exp["id"] == expense_id:
                exp["amount"] = float(request.form.get("amount"))
                exp["category"] = request.form.get("category")
                exp["date"] = request.form.get("date")
                exp["description"] = request.form.get("description")
                break
        save_expenses(expenses)
        return redirect("/expenses")
    
    expense_to_edit = next((exp for exp in expenses if exp["id"] == expense_id), None)
    if not expense_to_edit:
        return "Expense not found", 404
    
    return render_template("edit_expense.html", expense=expense_to_edit, categories=CATEGORIES)

if __name__ == "__main__":
    app.run(debug=True)
