class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        self.author._articles.append(self)
        self.author._magazines.add(magazine)
        self.magazine._articles.append(self)
        self.magazine._contributors.add(author)
        
    
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

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise TypeError('Author must be an instance of the Author class.')
        self._author = author

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise TypeError('Magazine must be an instance of the Magazine class.')
        self._magazine = magazine

class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []
        self._magazines = set()


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
        return self._articles

    def magazines(self):
        return list(self._magazines)

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        if article not in self._articles:
            self._articles.append(article)
        if magazine not in self._magazines:
            self._magazines.add(magazine)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        self._contributors = set()
        Magazine.all.append(self)

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
        return self._articles

    def contributors(self):
        return list(self._contributors)

    def article_titles(self):
        if self._articles:
            return [article.title for article in self._articles]
        else:
            return None

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1
        
        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        if contributing_authors:
            return contributing_authors
        else: 
            return None
        
    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        magazine_counts = {}
        for magazine in cls.all:
            magazine_counts[magazine] = len(magazine._articles)
        if all(count == 0 for count in magazine_counts.values()):
            return None
        top_magazine = max(magazine_counts, key=magazine_counts.get)
        return top_magazine
    

