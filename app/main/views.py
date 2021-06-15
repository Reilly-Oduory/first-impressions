from datetime import date
from . import main
from flask import render_template,url_for,redirect,request,abort
from flask_login import login_required, current_user
import markdown2
from ..models import Pitch, User
from .forms import PitchForm

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

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html', user = user)

@main.route('/pitch/new', methods = ["GET","POST"])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.title.data
        category = form.category.data

        new_pitch = Pitch(title,category,content,date())

        new_pitch.save_pitch()
        return redirect(url_for(main.profile))
    
    title = 'New Pitch'
    return render_template('new_pitch.html', title = title, pitch_form = form)

@main.route('/pitch/<int:id>')
def single_pitch(id):
    pitch = Pitch.query.get(id)
    if pitch is None:
        abort(404)
    format_pitch = markdown2.markdown(pitch.content, extras=["code-friendly", "fenced-code-blocks"])

    return render_template('pitch.html', pitch = pitch, format_pitch = format_pitch)