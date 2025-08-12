from flask import Flask, render_template, request, url_for, redirect, flash
from SECRET import web_app_secret_key
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

application = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static")
)

# Тех. Обслуживание
MAINTENANCE_MODE = False # переключатель техобслуживания


# Конфиг
application.config.update(SECRET_KEY=web_app_secret_key)

# Меню
menu = [
    {"title": "Главная", "url": "/home"},
    {"title": "О колледже", "url": "/about"},
    {"title": "Направления обучения", "url": "/programs"},
    {"title": "Контакты", "url": "/contacts"},
    {"title": "Новости", "url": "/news"},
    {"title": "Поступить", "url": "/register"}
]


@application.before_request
def check_maintenance():
    # Если включен режим техобслуживания и пользователь не на странице /maintenance
    if MAINTENANCE_MODE:
        # Разрешаем доступ только к странице техобслуживания и статике
        if request.endpoint not in ('maintenance', 'static'):
            return redirect(url_for('maintenance'))


@application.route('/technicalwork')
def maintenance():
    return render_template('technicalwork.html')  # HTML с сообщением «Сайт на техобслуживании»


# --- Маршруты ---
@application.route("/")
@application.route("/home")
@application.route("/index")
def index():
    return render_template("index.html", title="Главная", menu=menu)

@application.route("/about")
def about():
    return render_template("about.html", title="О колледже", menu=menu)

@application.route("/programs")
def programs():
    return render_template("programs.html", title="Направления обучения", menu=menu)

@application.route("/contacts")
def contacts():
    return render_template("contacts.html", title="Контакты", menu=menu)

@application.route("/news")
def news():
    return render_template("news.html", title="Новости", menu=menu)

@application.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        flash("Извините, но мест больше нет")
        return redirect(url_for("register"))
    return render_template("register.html", title="Регистрация", menu=menu)

# Обработка ошибки 404
@application.errorhandler(404)
def error_404(error):
    return render_template("error_404.html", title="Страница не найдена", menu=menu), 404

# Для Passenger (хостинг)

# Для локального запуска
if __name__ == "__main__":
    application.run(host='0.0.0.0')



