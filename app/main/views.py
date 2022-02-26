from flask import render_template,request,redirect,url_for
from .import main
from ..requests import get_news,get_articles


# Views
@main.route('/',methods=[ 'POST','GET'])
def index():
    '''
    View root page function that returns the index page and its data
    '''

    data = {
        "title":"News API",
        "heading": "News"
    }
    sources = get_news()
    articles= get_articles('creative')
    
    
    return render_template('index.html',context=data,sources= sources,article=articles)