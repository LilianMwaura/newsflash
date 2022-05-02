class Articles:
    """
    A class that generates new instances of news articles within news sources
    """
    
    def __init__(self,author, title, description, url, urlToImage, publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt