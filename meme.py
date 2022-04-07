"""Generate a meme using args in the shell."""
import os
import random
import argparse
from QuoteEngine import QuoteModel
from QuoteEngine import Ingestor
from MemeGenerator import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path  # path[0] add to be changed this here too

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Make a meme')
    parser.add_argument('--path', type=str, default=None,
                        help='path to the image')
    parser.add_argument('--body', type=str, default=None,
                        help='text for the meme')
    parser.add_argument('--author', type=str, default=None,
                        help='author of the text')

    args = parser.parse_args()

    # had to add this to path and delete the line above for this to work
    if(args.path):
        path = (args.path).split('=')[0]
    else:
        path = args.path

    try:
        _path = generate_meme(path, args.body, args.author)
        print(f"meme created in {_path}")
    except AttributeError:
        print("The path that you wrote had an issue")
