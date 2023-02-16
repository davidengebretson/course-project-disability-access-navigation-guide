from flask import Flask, render_template, request, jsonify

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
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/upload")
def upload():
    return render_template("upload.html", locations=LOCATIONS)

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

#Northcampus#
@app.route("/bondhall")
def bondhall():
    return render_template("campnav/northcampusnav/bondhall.html")

@app.route("/carvergym")
def carvergym():
    return render_template("campnav/northcampusnav/carvergym.html")

@app.route("/collegehall")
def collegehall():
    return render_template("campnav/northcampusnav/collegehall.html")

@app.route("/fraserhall")
def fraserhall():
    return render_template("campnav/northcampusnav/fraserhall.html")

@app.route("/haggardhall")
def haggardhall():
    return render_template("campnav/northcampusnav/haggardhall.html")

@app.route("/humanitiesbuilding")
def humanitiesbuilding():
    return render_template("campnav/northcampusnav/humanitiesbuilding.html")

@app.route("/millerhall")
def millerhall():
    return render_template("campnav/northcampusnav/millerhall.html")

@app.route("/oldmain")
def oldmain():
    return render_template("campnav/northcampusnav/oldmain.html")

@app.route("/performingartscenter")
def performingartscenter():
    return render_template("campnav/northcampusnav/performingartscenter.html")

@app.route("/wilsonlibrary")
def wilsonlibrary():
    return render_template("campnav/northcampusnav/wilsonlibrary.html")
#Midcampus#
@app.route("/arntzenhall")
def arntzenhall():
    return render_template("campnav/midcampusnav/arntzenhall.html")
#Arntzenhall
@app.route("/ah1")
def ah1():
    return render_template("campnav/midcampusnav/arntzenhall/ah1.html")
@app.route("/ah2")
def ah2():
    return render_template("campnav/midcampusnav/arntzenhall/ah2.html")
@app.route("/ah3")
def ah3():
    return render_template("campnav/midcampusnav/arntzenhall/ah3.html")
@app.route("/ah4")
def ah4():
    return render_template("campnav/midcampusnav/arntzenhall/ah4.html")
@app.route("/ah5")
def ah5():
    return render_template("campnav/midcampusnav/arntzenhall/ah5.html")
@app.route("/basement")
def basement():
    return render_template("campnav/midcampusnav/arntzenhall/basement.html")
@app.route("/concourse")
def consourse():
    return render_template("campnav/midcampusnav/arntzenhall/concourse.html")
@app.route("/penthouse")
def penthouse():
    return render_template("campnav/midcampusnav/arntzenhall/penthouse.html")

@app.route("/upload_status", methods=['POST'])
def checkUpload():
    if request.form.get('entry-date') and request.form.get('location') and request.form.get('desc'):
        return render_template("success.html")
    else:
        return render_template("failure.html")

#SouthCampus#
@app.route("/academiceast")
def academiceast():
    return render_template("campnav/southcampusnav/academiceast.html")

@app.route("/academicwest")
def academicwest():
    return render_template("campnav/southcampusnav/academicwest.html")

@app.route("/communicationsfacility")
def communicationsfacility():
    return render_template("campnav/southcampusnav/communicationsfacility.html")

#CF Halls#
@app.route("/cfbasement")
def cfbasement():
    return render_template("campnav/southcampusnav/cffloors/cfbasement.html")
@app.route("/cf1")
def cf1():
    return render_template("campnav/southcampusnav/cffloors/cf1.html")
@app.route("/cf2")
def cf2():
    return render_template("campnav/southcampusnav/cffloors/cf2.html")
@app.route("/cf3")
def cf3():
    return render_template("campnav/southcampusnav/cffloors/cf3.html")
@app.route("/cf4")
def cf4():
    return render_template("campnav/southcampusnav/cffloors/cf4.html")

@app.route("/sample")
def sample():
    return render_template("campnav/sampleroom.html")