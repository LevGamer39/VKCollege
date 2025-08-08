from flask import Flask, render_template, g, request, request_started, url_for, redirect, flash, session
import os
import datetime
app = Flask("VKCollege")
app.config.update(DEBUG=True)

menu = [
        {
            "title": "Главная",
            "url": "/home"
        },
        {
            "title": "Мероприятия",
            "url": "/events/events"
        },
        {
            "title": "Галерея",
            "url": "/events/gallery"
        }
]

def getSliderPaths(configFileName):
    with open(configFileName, "r") as f:
        ls = f.read().replace("\n", "")
        return ls.split(",")





@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("index.html", menu=menu)



@app.errorhandler(404)
def error_404(error): 
    return render_template("error_404.html", menu=menu)

if __name__ == "__main__":
    app.run("0.0.0.0", port=4221, debug=app.config.get("DEBUG"))
