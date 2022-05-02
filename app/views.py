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

@app.route('/articles/<int:articles_id>')
def articles(articles_id):
    
    '''
    View movie page function that returns the movie details page and its data
    '''

    return render_template('articles.html', id = articles_id)