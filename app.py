from flask import Flask, render_template, request, jsonify, flash, redirect
from werkzeug.utils import secure_filename
import pymongo
import os


MONGO_URI = open("config.txt").read()
client = pymongo.MongoClient(MONGO_URI)
db = client['DANG-DB']
data = db.get_collection("building-data")

app = Flask(__name__)

upload_folder = os.path.join('static', 'uploads')
app.config['UPLOAD'] = upload_folder

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

@app.route("/upload_status", methods=['POST'])
def checkUpload():
    date = request.form.get('entry-date')
    location = request.form.get('location')
    desc = request.form.get('desc')
    
    f = request.files['file']
        
    # If all required fields are supplied, insert into db collection
    if date and location and f.filename and desc:
        f = request.files['file']
        fname = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD'], fname))
        
        data.insert_one({
            "date": date,
            "location": location,
            "filename": f.filename,
            "desc": desc
        })
        
        # retrieve data just inserted
        entry = data.find_one({
            "date": date,
            "location": location,
            "filename":f.filename,
            "desc": desc
        })
        print(entry)
        return render_template("success.html", entry = entry, file = os.path.join(app.config['UPLOAD'], fname))
    else:
        return render_template("failure.html")

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

#BH Floors#
@app.route("/bh1")
def bh1():
    return render_template("campnav/northcampusnav/bhfloors/bh1.html")
@app.route("/bh_mez")
def bh_mez():
    return render_template("campnav/northcampusnav/bhfloors/bh_mez.html")
@app.route("/bh2")
def bh2():
    return render_template("campnav/northcampusnav/bhfloors/bh2.html")
@app.route("/bh3")
def bh3():
    return render_template("campnav/northcampusnav/bhfloors/bh3.html")
@app.route("/bh4")
def bh4():
    return render_template("campnav/northcampusnav/bhfloors/bh4.html")
@app.route("/bh_pent")
def bh_pent():
    return render_template("campnav/northcampusnav/bhfloors/bh_pent.html")

#CV Floors#
@app.route("/cv1")
def cv1():
    return render_template("campnav/northcampusnav/cvfloors/cv1.html")
@app.route("/cv2")
def cv2():
    return render_template("campnav/northcampusnav/cvfloors/cv2.html")
@app.route("/cv3")
def cv3():
    return render_template("campnav/northcampusnav/cvfloors/cv3.html")

#CH Floors#
@app.route("/ch_base")
def ch_base():
    return render_template("campnav/northcampusnav/chfloors/ch_base.html")
@app.route("/ch1")
def ch1():
    return render_template("campnav/northcampusnav/chfloors/ch1.html")
@app.route("/ch2")
def ch2():
    return render_template("campnav/northcampusnav/chfloors/ch2.html")
@app.route("/ch3")
def ch3():
    return render_template("campnav/northcampusnav/chfloors/ch3.html")

#FR Floors#
@app.route("/fr_base")
def fr_base():
    return render_template("campnav/northcampusnav/frfloors/fr_base.html")
@app.route("/fr1")
def fr1():
    return render_template("campnav/northcampusnav/frfloors/fr1.html")
@app.route("/fr2")
def fr2():
    return render_template("campnav/northcampusnav/frfloors/fr2.html")

#HH Floors#
@app.route("/hh1")
def hh1():
    return render_template("campnav/northcampusnav/hhfloors/hh1.html")
@app.route("/hh2")
def hh2():
    return render_template("campnav/northcampusnav/hhfloors/hh2.html")
@app.route("/hh3")
def hh3():
    return render_template("campnav/northcampusnav/hhfloors/hh3.html")
@app.route("/hh_pent")
def hh_pent():
    return render_template("campnav/northcampusnav/hhfloors/hh_pent.html")

#HU Floors#
@app.route("/hu1")
def hu1():
    return render_template("campnav/northcampusnav/hufloors/hu1.html")
@app.route("/hu2")
def hu2():
    return render_template("campnav/northcampusnav/hufloors/hu2.html")
@app.route("/hu3")
def hu3():
    return render_template("campnav/northcampusnav/hufloors/hu3.html")

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

#OM Floors#
@app.route("/om1")
def om1():
    return render_template("campnav/northcampusnav/omfloors/om1.html")
@app.route("/om2")
def om2():
    return render_template("campnav/northcampusnav/omfloors/om2.html")
@app.route("/om3")
def om3():
    return render_template("campnav/northcampusnav/omfloors/om3.html")
@app.route("/om4")
def om4():
    return render_template("campnav/northcampusnav/omfloors/om4.html")
@app.route("/om5")
def om5():
    return render_template("campnav/northcampusnav/omfloors/om5.html")

#PAC Floors#
@app.route("/pac_base")
def pac_base():
    return render_template("campnav/northcampusnav/pacfloors/pac_base.html")
@app.route("/pac1")
def pac1():
    return render_template("campnav/northcampusnav/pacfloors/pac1.html")
@app.route("/pac2")
def pac2():
    return render_template("campnav/northcampusnav/pacfloors/pac2.html")
@app.route("/pac3")
def pac3():
    return render_template("campnav/northcampusnav/pacfloors/pac3.html")
@app.route("/pac4")
def pac4():
    return render_template("campnav/northcampusnav/pacfloors/pac4.html")

#WL Floors#
@app.route("/wl1")
def wl1():
    return render_template("campnav/northcampusnav/wlfloors/wl1.html")
@app.route("/wl2")
def wl2():
    return render_template("campnav/northcampusnav/wlfloors/wl2.html")
@app.route("/wl3")
def wl3():
    return render_template("campnav/northcampusnav/wlfloors/wl3.html")
@app.route("/wl4")
def wl4():
    return render_template("campnav/northcampusnav/wlfloors/wl4.html")
@app.route("/wl5")
def wl5():
    return render_template("campnav/northcampusnav/wlfloors/wl5.html")
@app.route("/wl6")
def wl6():
    return render_template("campnav/northcampusnav/wlfloors/wl6.html")

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

#BI Floors#

#ES Floors#

#FA Floors#

#IS Floors#

#CB Floors#

#PH Floors#

#ET Floors#

#SL Floors#
@app.route("/sl1")
def sl1():
    return render_template("campnav/midcampusnav/slfloors/sl1.html")
@app.route("/sl2")
def sl2():
    return render_template("campnav/midcampusnav/slfloors/sl2.html")

#SL Classrooms#
@app.route("/sl110")
def sl110():
    return render_template("campnav/midcampusnav/slfloors/sl_classrooms/sl110.html")
@app.route("/sl120")
def sl120():
    return render_template("campnav/midcampusnav/slfloors/sl_classrooms/sl120.html")
@app.route("/sl130")
def sl130():
    return render_template("campnav/midcampusnav/slfloors/sl_classrooms/sl130.html")
@app.route("/sl140")
def sl140():
    return render_template("campnav/midcampusnav/slfloors/sl_classrooms/sl140.html")
@app.route("/sl150")
def sl150():
    return render_template("campnav/midcampusnav/slfloors/sl_classrooms/sl150.html")
@app.route("/sl210")
def sl210():
    return render_template("campnav/midcampusnav/slfloors/sl_classrooms/sl210.html")
@app.route("/sl220")
def sl220():
    return render_template("campnav/midcampusnav/slfloors/sl_classrooms/sl220.html")
@app.route("/sl230")
def sl230():
    return render_template("campnav/midcampusnav/slfloors/sl_classrooms/sl230.html")
@app.route("/sl240n")
def sl240n():
    return render_template("campnav/midcampusnav/slfloors/sl_classrooms/sl240n.html")
@app.route("/sl240s")
def sl240s():
    return render_template("campnav/midcampusnav/slfloors/sl_classrooms/sl240s.html")

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

#AW Floors
@app.route("/aw2")
def aw2():
    return render_template("campnav/southcampusnav/awfloors/aw2.html")
@app.route("/aw3")
def aw3():
    return render_template("campnav/southcampusnav/awfloors/aw3.html")
@app.route("/aw4")
def aw4():
    return render_template("campnav/southcampusnav/awfloors/aw4.html")

#AW Classrooms#
@app.route("/aw203")
def aw203():
    return render_template("campnav/southcampusnav/awfloors/aw_classrooms/aw203.html")
@app.route("/aw204")
def aw204():
    return render_template("campnav/southcampusnav/awfloors/aw_classrooms/aw204.html")
@app.route("/aw205")
def aw205():
    return render_template("campnav/southcampusnav/awfloors/aw_classrooms/aw205.html")
@app.route("/aw210")
def aw210():
    return render_template("campnav/southcampusnav/awfloors/aw_classrooms/aw210.html")
@app.route("/aw302")
def aw302():
    return render_template("campnav/southcampusnav/awfloors/aw_classrooms/aw302.html")
@app.route("/aw303")
def aw303():
    return render_template("campnav/southcampusnav/awfloors/aw_classrooms/aw303.html")
@app.route("/aw304")
def aw304():
    return render_template("campnav/southcampusnav/awfloors/aw_classrooms/aw304.html")
@app.route("/aw305")
def aw305():
    return render_template("campnav/southcampusnav/awfloors/aw_classrooms/aw305.html")
@app.route("/aw306")
def aw306():
    return render_template("campnav/southcampusnav/awfloors/aw_classrooms/aw306.html")
@app.route("/aw402")
def aw402():
    return render_template("campnav/southcampusnav/awfloors/aw_classrooms/aw402.html")
@app.route("/aw404")
def aw404():
    return render_template("campnav/southcampusnav/awfloors/aw_classrooms/aw404.html")
@app.route("/aw406")
def aw406():
    return render_template("campnav/southcampusnav/awfloors/aw_classrooms/aw406.html")
@app.route("/aw408")
def aw408():
    return render_template("campnav/southcampusnav/awfloors/aw_classrooms/aw408.html")
@app.route("/aw410")
def aw410():
    return render_template("campnav/southcampusnav/awfloors/aw_classrooms/aw410.html")
@app.route("/aw412")
def aw412():
    return render_template("campnav/southcampusnav/awfloors/aw_classrooms/aw412.html")
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
@app.route("/samplefloor")
def samplefloor():
    return render_template("campnav/samplefloor.html")