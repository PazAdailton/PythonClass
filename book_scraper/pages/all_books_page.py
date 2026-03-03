from PythonClass.book_scraper.locators.book_page_locators import BookPageLocators
from PythonClass.book_scraper.parsers.books import ParserBooks
from bs4 import BeautifulSoup


class AllBooksPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')


    @property
    def all_books(self):
        locator = BookPageLocators.BOOK_PAGE
        return [ParserBooks(e) for e in self.soup.select_one(locator)]
