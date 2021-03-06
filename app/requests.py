import urllib.request,json
from .models import News,Articles

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

def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:        
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')

        if url:
            news_object = News(id,name,description,url,category,language)
            news_results.append(news_object)

    return news_results

def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = article_url.format(category,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = article_process_results(article_results_list)


    return article_results

def article_process_results(article_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain news details

    Returns :
        article_results: A list of article objects
    '''
    article_results = []
    for article_item in article_list:        
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        if url:
            article_object= Articles(author,title,description,url,urlToImage,publishedAt,content)
            article_results.append(article_object)

    return article_results
