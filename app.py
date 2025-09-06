from flask import Flask

# Create the Flask app
app = Flask(__name__)

# Home Page
@app.route('/')
def index():
    return "MUHCS Cash Management System is running!"

if __name__ == "__main__":
    app.run(debug=True)
