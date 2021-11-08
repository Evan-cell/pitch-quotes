from flask import render_template,request,redirect,url_for
from . import main
# from flask_login import login_required

# from .forms import ReviewForm
# from ..models import Review


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    message = 'Hello World'
    return render_template('index.html',message = message)
@main.route('/PITCHER/comment/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    

    
    return render_template('comment.html')