"""Import the quotes from a txt file."""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Imports a txt file.

    Separates the quote from the author and saves the quote.
    """

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Do the work for the class."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []

        # https://www.pythontutorial.net/python-basics/
        # python-read-text-file/
        lines = []
        with open(path) as f:
            lines = f.readlines()

        for text in lines:
            line = text.split('-')
            new_quote = QuoteModel(line[0].strip(), line[1].strip())
            quotes.append(new_quote)

        return quotes
