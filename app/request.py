from app import app
import urllib.request,json
from .models import articles

Articles= articles.Articles
# Getting api key
api_key = app.config['ARTICLES_API_KEY']

# Getting the movie base url
base_url = app.config["ARTICLES_API_BASE_URL"]

def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['results']:
            articles_results_list = get_articles_response['results']
            articles_results = process_results(articles_results_list)


    return articles_results
    