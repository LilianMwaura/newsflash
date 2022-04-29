from turtle import title
from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "NewsFlash - Latest breaking news and information on top stories"
    return render_template('index.html',title=title)
@app.route('/article/<id>')
def article(id):
    
    
    articles = get_article(id)
    return render_template('article.html',articles=articles,id=id )