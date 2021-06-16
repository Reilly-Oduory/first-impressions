from datetime import date
from . import main
from flask import render_template,url_for,redirect,request,abort
from flask_login import login_required, current_user
import markdown2
from ..models import Pitch, User, Comment
from .forms import PitchForm, CommentForm

@main.route('/')
def index():
    
    title = 'First Impressions'
    pitches = Pitch.query.all()
    
    return render_template('index.html', title = title, pitches = pitches)


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
    pitches = Pitch.get_user_pitches(user.get_id())
    if user is None:
        abort(404)

    return render_template('profile/profile.html', user = user, pitches = pitches)

@main.route('/pitch/new', methods = ["GET","POST"])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.title.data
        category = form.category.data
        new_pitch = Pitch(current_user.get_id(), title,category,content, date.today())
        new_pitch.save_pitch()
        return redirect(url_for('.profile',uname=current_user.username))
    
    title = 'New Pitch'
    return render_template('new_pitch.html', title = title, pitch_form = form, user = current_user)

@main.route('/pitch/<int:id>')
def pitch(id):
    pitch = Pitch.query.filter_by(id = id).first()
    title = f'{pitch.title}'
    comments = Comment.get_comments(pitch.id)

    return render_template('pitch.html', title = title, pitch = pitch, comments = comments)

@main.route('/pitch/comment/new/<int:id>', methods=["GET","POST"])
@login_required
def new_comment(id):
    comment_form = CommentForm()
    pitch = Pitch.get_selected_pitches(id)
    if comment_form.validate_on_submit():
        title = comment_form.title.data
        comment_content = comment_form.comment_content.data

        new_comment = Comment(current_user.get_id(),pitch.id,title, comment_content)
        new_comment.save_comment()
        return redirect(url_for('main.pitch', id = pitch.id))

    title = 'Comment'    
    return render_template('new_comment.html', comment_form = comment_form, pitch = pitch, title = title)