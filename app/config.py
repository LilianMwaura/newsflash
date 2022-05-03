class Config:
    '''
    General configuration parent class
    '''
    ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey=5ede76ca7fb24805a3b16ea7656b3da9'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

class Config:
    '''
    General configuration parent class
    '''
    ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'

