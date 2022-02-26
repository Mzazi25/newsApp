from flask import render_template,request,redirect,url_for
from .. import main
from ..requests import get_news
import app

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    data = {
        "title":"News API",
        "heading": "News"
    }
    sources = get_news()
    
    
    return render_template('index.html',context=data,sources= sources)