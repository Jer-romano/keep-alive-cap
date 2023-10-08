import os, atexit
from flask import Flask, redirect, render_template
from apscheduler.schedulers.background import BackgroundScheduler
from helpers import make_request


scheduler = BackgroundScheduler()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)
app.app_context().push()

@app.route("/")
def homepage():
    return render_template("base.html")



scheduler.add_job(make_request, "interval", minutes=12)
scheduler.start()


atexit.register(lambda: scheduler.shutdown()) #shutdown scheduler on app exit