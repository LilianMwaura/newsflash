class Source:
    """
    A class that generates instances of various news sources
    """
    def __init__(self,id, name, description, url, category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category