from flask import Flask, render_template, request, url_for, redirect, flash
from SECRET import web_app_secret_key, web_app_debug
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static")
)

# Конфиг
app.config.update(SECRET_KEY=web_app_secret_key, DEBUG=web_app_debug)

# Меню
menu = [
    {"title": "Главная", "url": "/home"},
    {"title": "О колледже", "url": "/about"},
    {"title": "Направления обучения", "url": "/programs"},
    {"title": "Контакты", "url": "/contacts"},
    {"title": "Новости", "url": "/news"},
    {"title": "Поступить", "url": "/register"}
]

# --- Маршруты ---
@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("index.html", title="Главная", menu=menu)

@app.route("/about")
def about():
    return render_template("about.html", title="О колледже", menu=menu)

@app.route("/programs")
def programs():
    return render_template("programs.html", title="Направления обучения", menu=menu)

@app.route("/contacts")
def contacts():
    return render_template("contacts.html", title="Контакты", menu=menu)

@app.route("/news")
def news():
    return render_template("news.html", title="Новости", menu=menu)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        flash("Извините, но мест больше нет")
        return redirect(url_for("register"))
    return render_template("register.html", title="Регистрация", menu=menu)

# Обработка ошибки 404
@app.errorhandler(404)
def error_404(error):
    return render_template("error_404.html", title="Страница не найдена", menu=menu), 404

# Для Passenger (хостинг)
application = app

# Для локального запуска
if __name__ == "__main__":
    app.run("0.0.0.0", port=4221, debug=app.config.get("DEBUG"))



