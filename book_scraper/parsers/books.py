from PythonClass.book_scraper.locators.book_locators import BookLocators

class ParserBooks:

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name}'

    @property
    def name(self):
        locator = BookLocators.NAME
        return self.parent.select_one(locator).string


    @property
    def link(self):
        locator = BookLocators.LINK
        return self.parent.select_one(locator).string

    @property
    def rating(self):
        locator = BookLocators.RATING
        return self.parent.select_one(locator).string

    @property
    def price(self):
        locator = BookLocators.PRICE
        return self.parent.select_one(locator).string



