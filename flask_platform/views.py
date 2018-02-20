from flask import render_template

from flask_platform import app
from systeminfo_cookiecutter import systeminfo_cookiecutter as s


@app.route('/')
def index():
    returnDict = {}
    p = s.get_platform() 
#    print(p)
    returnDict['platform'] = p
    returnDict['title'] = 'Home'
    return render_template("index.html", **returnDict)
