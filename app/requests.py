import urllib.request,json
from .models import News

# Getting api key
api_key = None
# Getting the News base url
base_url = None
#Getting the Article url
article_url =None

def configure_request(app):
    global api_key,base_url, article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config["ARTICLES_API_BASE_URL"]