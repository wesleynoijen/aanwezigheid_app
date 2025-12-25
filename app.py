# DAILY USE
# Run the terminal command $env:FLASK_APP = "app.py" (tells the active development environment which app to run.)
# Run the terminal command "flask run" (starts the app)
# Ctrl + C (stops the app)

# Import Flask module
from flask import Flask, render_template, jsonify
# Import JSON module
import json
# Import OS module
import os

# Create a Flask object
# __name__ makes sure Flask can find the location of the app (because the app can be run separately or as a module)
app = Flask(__name__)

# Makes sure the server restarts everytime the command "flask run" is used so that changes become visible on the web
if __name__ == "__main__":
    app.run(debug=True)

# View function that binds one or multiple urls to a function
# Here "/" is connected to the function home() (the function can have any name you want, this name makes the most sense as "/" is the homepage)
# Functions can return text for example: return 'Hello World!', but they can also return html like: return '''<h1>Hello World!</h1>'''
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/toggle/<person>/<day>')
def toggle(person, day):
    path = 'static/data/availability.json'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    # Load of create
    try:
        with open(path) as f:
            data = json.load(f)
    except:
        data = {}
    
    # Toggle
    if person not in data:
        data[person] = {}
    data[person][day] = not data[person].get(day, False)
    
    # Save
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/data')
def get_data():
    path = 'static/data/availability.json'
    try:
        with open(path) as f:
            return jsonify(json.load(f))
    except:
        return jsonify({})
    
@app.route('/reset')
def reset_all():
    path = 'static/data/availability.json'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    # Reset naar expliciet ALLE false
    data = {
        "Joey": {"Maandag": False, "Dinsdag": False, "Woensdag": False, "Donderdag": False, "Vrijdag": False, "Zaterdag": False, "Zondag": False},
        "Wesley": {"Maandag": False, "Dinsdag": False, "Woensdag": False, "Donderdag": False, "Vrijdag": False, "Zaterdag": False, "Zondag": False},
        "Sieb": {"Maandag": False, "Dinsdag": False, "Woensdag": False, "Donderdag": False, "Vrijdag": False, "Zaterdag": False, "Zondag": False},
        "Steef": {"Maandag": False, "Dinsdag": False, "Woensdag": False, "Donderdag": False, "Vrijdag": False, "Zaterdag": False, "Zondag": False}
    }
    
    # Save
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    
    return jsonify(data)
