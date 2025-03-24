Expense Tracker

📌 Overview

This is a simple Expense Tracker web application built using Flask (Python), HTML, CSS, and JSON as the database. It allows users to add, view, and track expenses easily.

🛠️ Tech Stack

Backend: Flask (Python)

Frontend: HTML, CSS

Database: JSON (data.json)

📂 Project Structure

📂 expense_tracker/
│── 📄 app.py  (Flask Backend)
│── 📄 data.json  (Stores expenses)
│── 📂 templates/  (HTML Templates)
│   ├── 📄 index.html  (Form to Add Expenses)
│   ├── 📄 expenses.html  (Displays Expenses)
│── 📂 static/  (CSS files)
│   ├── 📄 style.css  (Styling)
│── 📄 README.md  (Project Documentation)
│── 📄 requirements.txt  (Dependencies)

🚀 Features

✅ Add expenses with amount, category, date, and description✅ View a list of all expenses✅ See the total expenses calculated dynamically✅ Data is stored in a JSON file (no database required!)

🔧 Installation & Setup

Clone the repository

git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker

Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Run the Flask application

python app.py

Open in browser

http://127.0.0.1:5000/

🖥️ Usage

Go to the homepage (/) to add a new expense.

Click 'View Expenses' to see the list of recorded expenses and the total spent amount.

📝 To-Do (Future Improvements)

✅ Add ability to delete/edit expenses.

✅ Filter expenses by category/date.

✅ Add authentication (user accounts).

✅ Improve UI with JavaScript.

📜 License

This project is open-source and available under the MIT License.

🚀 Happy Coding! 😊

