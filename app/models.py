class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,description,url,category,language):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language

class Articles:
    "Articles class to define Articles Objects"
    def __init__(self,author,title,description,url,urlToImage,publishedAt,content):
        self.author= author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
