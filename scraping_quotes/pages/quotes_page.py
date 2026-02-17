from scraping_quotes.locators.quotes_page_locators import QuotesPageLocators
from scraping_quotes.parsers.quotes import ParserQuotes
from bs4 import BeautifulSoup


class QuotesPages:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')


    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quote_tags = self.soup.select(locator)
        return [ParserQuotes(e) for e in quote_tags]


