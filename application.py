from flask import Flask
from flask import render_template, redirect, request
from datetime import datetime


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page, with a list of all polls."""
    return render_template('index.html', title='Home Automation', year=datetime.now().year)


@app.route('/about')
def about():
    """Renders the home page, with a list of all polls."""
    return render_template( 'about.html', title='Home Automation', year=datetime.now().year)


@app.route('/contact')
def contact():
    """Renders the home page, with a list of all polls."""
    return render_template( 'contact.html', title='Home Automation', year=datetime.now().year)


if __name__ == "__main__":
    app.run(debug=True)  