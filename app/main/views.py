from . import main
from flask import render_template,url_for

@main.route('/')
def index():
    title = 'First Impressions'
    return render_template('index.html', title = title)
