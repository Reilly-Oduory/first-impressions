from . import main
from flask import render_template,url_for
from flask_login import login_required

@main.route('/')
def index():
    
    title = 'First Impressions'
    
    return render_template('index.html', title = title)


@main.route('/category/pickup')
def pickup():
    
    title = 'Pick Up lines Galore'

    return render_template('category/pickup.html', title = title)

@main.route('/category/interview')
def interview():

    title = 'Impress the interviewer guaranteed'

    return render_template('category/interview.html', title = title)

@main.route('/category/product')
def product():

    title = 'Sell your prduct assurance'

    return render_template('category/product.html', title = title)

@main.route('/category/business')
def business():
    
    title = 'Make an incredible business pitch'

    return render_template('category/business.html', title = title)