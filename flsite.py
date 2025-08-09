from flask import Flask, render_template, request, url_for
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

app = Flask("VKCollege", template_folder=str(BASE_DIR / 'templates'), static_folder=str(BASE_DIR / 'static'))
app.config.update(DEBUG=True, SECRET_KEY='dev-secret')

menu = [
    {"title": "Главная", "url": "/home"},
    {"title": "Мероприятия", "url": "/events/events"},
    {"title": "Галерея", "url": "/events/gallery"}
]

def getSliderPaths(configFileName='slider.cfg'):
    p = BASE_DIR / configFileName
    if not p.exists():
        return []
    content = p.read_text(encoding='utf-8').strip()
    return [s.strip() for s in content.split(',') if s.strip()]

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    slides = getSliderPaths()
    return render_template('index.html', menu=menu, slides=slides)

@app.route('/events/events')
def events_list():
    events = [
        {"title": "Посвящение в студенты", "date": "2025-09-01", "desc": "Торжественное мероприятие"},
        {"title": "День открытых дверей", "date": "2025-10-10", "desc": "Приходите с друзьями"}
    ]
    return render_template('events/events.html', menu=menu, events=events)

@app.route('/events/gallery')
def gallery():
    images_dir = BASE_DIR / 'static' / 'images'
    imgs = []
    if images_dir.exists():
        for p in images_dir.iterdir():
            if p.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
                imgs.append(str(Path('static') / 'images' / p.name))
    return render_template('events/gallery.html', menu=menu, images=imgs)

@app.errorhandler(404)
def error_404(error):
    return render_template('error_404.html', menu=menu), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4221, debug=True)