class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError('Title must be a string.')
        if not (5 <= len(title) <= 50):
            raise ValueError('Title must be between 5 and 50 characters, inclusive.')
        if hasattr(self, '_title'):
            raise AttributeError("Title cannot be changed after it has been set.")
        self._title = title
        
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name) <= 0:
            raise ValueError("Name must be longer than 0 characters.")
        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be changed after it has been set.")
        self._name = name

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string.')
        if not (2 <= len(name) <= 16):
            raise ValueError('Name must be between 2 and 16 characters, inclusive.')
        self._name = name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if not isinstance(category, str):
            raise TypeError('Category must be a string.')
        if len(category) <= 0:
            raise ValueError('Category must be longer than 0  characters.')
        self._category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass