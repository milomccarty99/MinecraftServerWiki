import os
import markdown
from flask import Flask

app = Flask(__name__)
wikipath = "Wiki/"

def getfolderpage(filepath):
    filestructure = os.listdir(wikipath + filepath)
    pageview = filepath
    for entry in filestructure:
        pageview = "<a href=" + os.path.join(filepath, entry) + ">" + entry + "</a>\n"
    return pageview

@app.route("/")
def hello_world():
    return getfolderpage("")

@app.route("/<randfile>")
def helper_function1(randfile):
   
    if (".md" in randfile):
        return open(wikipath+randfile)
    return getfolderpage(randfile)
