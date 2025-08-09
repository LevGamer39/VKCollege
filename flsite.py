from flask import Flask, render_template, g, request, request_started, url_for, redirect, flash, session
from SECRET import web_app_secret_key, web_app_debug


app = Flask("0")
app.config.update(SECRET_KEY=web_app_secret_key)
app.config.update(DEBUG=web_app_debug)
menu = [
        {
            "title": "Главная",
            "url": "/home"
        }
]

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("index.html", menu=menu)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        flash('Извините, но мест больше нет ')
        return redirect(url_for('register'))
    return render_template('register.html', title='Регистрация', menu=menu)

@app.errorhandler(404)
def error_404(error): 
    return render_template("error_404.html", menu=menu)




if __name__ == "__main__":
    app.run("0.0.0.0", port=4221, debug=app.config.get("DEBUG"))