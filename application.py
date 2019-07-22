from flask import Flask
from flask import render_template, redirect, request
from datetime import datetime

from models.solarPanels import SolarPanels
from models.bathroomWindow import BathroomWindow
from models.livingRoomWindow import LivingRoomWindow
from models.tv import Tv
from models.doctor import Doctor
from models.garageDoor import GarageDoor

sp = SolarPanels()
bw = BathroomWindow()
lw = LivingRoomWindow()
tv = Tv()
dc = Doctor()
gd = GarageDoor()


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page, with a list of all polls."""
    return render_template( 'index.html', title='Home Automation', year=datetime.now().year)


@app.route('/about')
def about():
    """Renders the home page, with a list of all polls."""
    return render_template( 'about.html', title='Home Automation', year=datetime.now().year)


@app.route('/contact')
def contact():
    """Renders the home page, with a list of all polls."""
    return render_template( 'contact.html', title='Home Automation', year=datetime.now().year)


@app.route('/home-automation')
def home_automation():
    """Renders the home page, with a list of all polls."""
    return render_template( 'home-automation.html', title='Home Automation', year=datetime.now().year)


@app.route('/activatepanels')
def activatepanels():
    """Renders the home page, with a list of all polls."""

    msg = sp.activate()

    return render_template( 'home-automation.html', title='Home Automation', year=datetime.now().year, message=msg)


@app.route('/deactivatepanels')
def deactivatepanels():
    """Renders the home page, with a list of all polls."""

    msg = sp.deActivate()

    return render_template( 'home-automation.html', title='Home Automation', year=datetime.now().year, message=msg)


@app.route('/openbathromwindow')
def openbathromwindow():
    """Renders the home page, with a list of all polls."""

    msg = bw.open()

    return render_template( 'home-automation.html', title='Home Automation', year=datetime.now().year, message=msg)


@app.route('/closebathromwindow')
def closebathromwindow():
    """Renders the home page, with a list of all polls."""

    msg = bw.close()

    return render_template( 'home-automation.html', title='Home Automation', year=datetime.now().year, message=msg)


@app.route('/openlivingroomwindows')
def openlivingroomwindows():
    """Renders the home page, with a list of all polls."""

    msg = lw.open()

    return render_template( 'home-automation.html', title='Home Automation', year=datetime.now().year, message=msg)


@app.route('/closelivingroomwindows')
def closelivingroomwindows():
    """Renders the home page, with a list of all polls."""

    msg = lw.close()

    return render_template( 'home-automation.html', title='Home Automation', year=datetime.now().year, message=msg)


@app.route('/tvon')
def tvon():
    """Renders the home page, with a list of all polls."""

    msg = tv.on()

    return render_template( 'home-automation.html', title='Home Automation', year=datetime.now().year, message=msg)


@app.route('/tvoff')
def tvoff():
    """Renders the home page, with a list of all polls."""

    msg = tv.off()

    return render_template( 'home-automation.html', title='Home Automation', year=datetime.now().year, message=msg)


@app.route('/opengaragedoor')
def opengaragedoor():
    """Renders the home page, with a list of all polls."""

    msg = gd.processOpening()

    return render_template( 'home-automation.html', title='Home Automation', year=datetime.now().year, message=msg)


@app.route('/calldoctor')
def calldoctor():
    """Renders the home page, with a list of all polls."""

    msg = dc.call()

    return render_template( 'home-automation.html', title='Home Automation', year=datetime.now().year, message=msg)


if __name__ == "__main__":
    app.run(debug=True)  