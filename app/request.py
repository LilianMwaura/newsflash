from app import app
import urllib.request,json
from .models import articles
from .models import source

# Getting api key
api_key = app.config['ARTICLES_API_KEY']

# Getting the articles base url
base_url = app.config["ARTICLES_API_BASE_URL"]

def get_sources():
    """
    A function that gets the json files from our url request
    """
    get_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results= None

        if get_sources_response["sources"]:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    """
    A function that processes the news sources results
   
    """
    source_results=[]
    for source_item in source_list:
        id = source_item.get("id")
        name = source_item.get("name")
        description = source_item.get("description")
        url = source_item.get("url")
        category = source_item.get("category")


        source_object=source.Source(id,name,description,url,category)
        source_results.append(source_object)

    return source_results

def get_articles(id):
    articles_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    print(articles_source_url)
    with urllib.request.urlopen(articles_source_url) as url:
        articles_source_data = url.read()
        articles_source_response = json.loads(articles_source_data)

        articles_source_results = None

        if articles_source_response['articles']:
            articles_source_list = articles_source_response['articles']
            articles_source_results = process_articles_results(articles_source_list)


    return articles_source_results

def process_articles_results(news):
    '''
    A function that processes the json files of news articles from api
    '''
    articles_source_results = []
    for article in news:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get ('publishedAt')

        if url:
            articles_objects = articles.Articles(author,title,description,url,urlToImage,publishedAt)
            articles_source_results.append(articles_objects)

    return articles_source_results