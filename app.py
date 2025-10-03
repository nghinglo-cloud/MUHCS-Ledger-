import os # Import the os module for path manipulation
from flask import Flask, render_template, redirect, url_for # Make sure render_template is imported

# Create the Flask app
# Explicitly tell Flask where to find the templates folder
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=os.path.join(basedir, 'templates'))

# --- Routes ---

# Home Page
@app.route('/')
def index():
    # Instead of just returning text, you probably want to redirect to the dashboard
    # return "MUHCS Cash Management System is running!"
    return redirect(url_for('dashboard')) # Redirects to the 'dashboard' function

# Dashboard Page (This is the route that was missing!)
@app.route('/dashboard')
def dashboard():
    # Placeholder for transactions data - replace with actual data retrieval later
    transactions = [
        {"id": 1, "date": "2025-03-01", "amount": 100, "description": "Consultation Fee"},
        {"id": 2, "date": "2025-03-02", "amount": 50, "description": "Medication Purchase"}
    ]
    return render_template('dashboard.html', transactions=transactions)

# --- End Routes ---

if __name__ == "__main__":
    app.run(debug=True)
