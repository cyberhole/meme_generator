"""Class to make a quote."""


class QuoteModel:
    """
    Class to create a quote.

    Arguments:
    body [{str}] = body of the quote.
    author [{str}] = author of the quote.
    """

    def __init__(self, body, author):
        """Construct the object: takes the body and author."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Represent the quote: body - author."""
        return f'{self.body} - {self.author}'
