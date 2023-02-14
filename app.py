from flask import Flask, render_template

app = Flask(__name__)

LOCATIONS = [
    "Communications Facility",
    "Old Main",
    "Bond Hall",
    "Miller Hall",
    "Nash Hall",
    "Viking Union",
]

@app.route("/")
def index():
    return render_template("index.html", locations=LOCATIONS)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/map")
def map():
    return render_template("map.html")

#Filtering Nav#
@app.route("/northcampus")
def northcampus():
    return render_template("campnav/northcampus.html")

@app.route("/midcampus")
def midcampus():
    return render_template("campnav/midcampus.html")

@app.route("/southcampus")
def southcampus():
    return render_template("campnav/southcampus.html")