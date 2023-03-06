from flask import Flask, render_template, request, jsonify, flash, redirect

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

@app.route("/map", methods=['GET', 'POST'])
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
@app.route("/biologybuilding")
def biologybuilding():
    return render_template("campnav/midcampusnav/biologybuilding.html")
@app.route("/environmentalscience")
def environmentalscience():
    return render_template("campnav/midcampusnav/environmentalscience.html")
@app.route("/fineartsbuilding")
def fineartsbuilding():
    return render_template("campnav/midcampusnav/fineartsbuilding.html")
@app.route("/morsehall")
def morsehall():
    return render_template("campnav/midcampusnav/morsehall.html")
@app.route("/parkshall")
def parkshall():
    return render_template("campnav/midcampusnav/parkshall.html")
@app.route("/rossengineeringtech")
def rossengineeringtech():
    return render_template("campnav/midcampusnav/rossengineeringtech.html")
@app.route("/sciencelecturebuilding")
def sciencelecturebuilding():
    return render_template("campnav/midcampusnav/sciencelecturebuilding.html")
@app.route("/interdiciplinaryscience")
def sinterdiciplinaryscience():
    return render_template("campnav/midcampusnav/interdiciplinaryscience.html")

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
@app.route("/samplefloor")
def samplefloor():
    return render_template("campnav/samplefloor.html")

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

#CF Floors#
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

#CF Classrooms#
@app.route("/cf023")
def cf023():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf023.html")
@app.route("/cf024")
def cf024():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf024.html")
@app.route("/cf025")
def cf025():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf025.html")
@app.route("/cf026")
def cf026():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf026.html")

@app.route("/cf105")
def cf105():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf105.html")
@app.route("/cf110")
def cf110():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf110.html")
@app.route("/cf115")
def cf115():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf115.html")
@app.route("/cf120")
def cf120():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf120.html")
@app.route("/cf125")
def cf125():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf125.html")
@app.route("/cf161")
def cf161():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf161.html")
@app.route("/cf162")
def cf162():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf162.html")
@app.route("/cf163")
def cf163():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf163.html")
@app.route("/cf164")
def cf164():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf164.html")
@app.route("/cf167")
def cf167():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf167.html")

@app.route("/cf224")
def cf224():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf224.html")
@app.route("/cf225")
def cf225():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf225.html")
@app.route("/cf226")
def cf226():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf226.html")
@app.route("/cf227")
def cf227():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf227.html")
@app.route("/cf229")
def cf229():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf229.html")
@app.route("/cf231")
def cf231():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf231.html")

@app.route("/cf312")
def cf312():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf312.html")
@app.route("/cf314")
def cf314():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf314.html")
@app.route("/cf316")
def cf316():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf316.html")

@app.route("/cf405")
def cf405():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf405.html")
@app.route("/cf420")
def cf420():
    return render_template("campnav/southcampusnav/cffloors/cf_classrooms/cf420.html")

#AI Floors
@app.route("/ai1")
def ai1():
    return render_template("campnav/southcampusnav/aifloors/ai1.html")
@app.route("/ai2")
def ai2():
    return render_template("campnav/southcampusnav/aifloors/ai2.html")
@app.route("/ai3")
def ai3():
    return render_template("campnav/southcampusnav/aifloors/ai3.html")
@app.route("/ai4")
def ai4():
    return render_template("campnav/southcampusnav/aifloors/ai4.html")
@app.route("/ai5")
def ai5():
    return render_template("campnav/southcampusnav/aifloors/ai5.html")

#SL Floors#
@app.route("/sl1")
def sl1():
    return render_template("campnav/midcampusnav/slfloors/sl1.html")
@app.route("/sl2")
def sl2():
    return render_template("campnav/midcampusnav/slfloors/sl2.html")


#MH Floors#
@app.route("/mhbasement")
def mhbasement():
    return render_template("campnav/northcampusnav/mhfloors/mhbasement.html")
@app.route("/mh1")
def mh1():
    return render_template("campnav/northcampusnav/mhfloors/mh1.html")
@app.route("/mh2")
def mh2():
    return render_template("campnav/northcampusnav/mhfloors/mh2.html")
@app.route("/mh3")
def mh3():
    return render_template("campnav/northcampusnav/mhfloors/mh3.html")


#Rooms for Testing#
@app.route("/sample1")
def sample1():
    return render_template("campnav/sampleclass1.html")
@app.route("/sample2")
def sample2():
    return render_template("campnav/sampleclass2.html")
@app.route("/sample3")
def sample3():
    return render_template("campnav/sampleclass3.html")

@app.route("/sample")
def sample():
    return render_template("campnav/sampleroom.html")