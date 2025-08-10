from flask import Flask, render_template, g, request, request_started, url_for, redirect, flash, session
from SECRET import web_app_secret_key

application = Flask(__name__)

app.config.update(SECRET_KEY=web_app_secret_key)

@application.route("/")
@application.route("/home")
@application.route("/index")
def index():
    return render_template("index.html")

@application.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        flash('Извините, но мест больше нет')
        return redirect(url_for('register'))
    return render_template('register.html', title='Регистрация')

if __name__ == "__main__":
   application.run(host='0.0.0.0')
