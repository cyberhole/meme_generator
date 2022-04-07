"""Creates the web page and shows the meme image there."""
import random
import os
import requests
from flask import Flask, render_template, abort, request
from QuoteEngine import Ingestor, QuoteModel
from MemeGenerator import MemeEngine
import QuoteEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []

    for file in quote_files:
        quote = Ingestor.parse(file)
        for quot in quote:
            quotes.append(quot)

    images_path = "./_data/photos/dog/"

    imgs = []

    # https://stackoverflow.com/questions/3964681/
    # find-all-files-in-a-directory-with-extension-txt-in-python
    for file in os.listdir(images_path):
        if file.endswith(".jpg"):
            imgs.append(images_path+file)

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # https://stackoverflow.com/questions/10434599/
    # get-the-data-received-in-a-flask-request

    temp_image = './_data/web_photos/web_photos.jpg'
    image_url = request.form['image_url']
    if not image_url:
        return render_template('meme_form.html')

    try:
        img_content = requests.get(image_url, stream=True).content
        with open(temp_image, 'wb') as f:
            f.write(img_content)
        image_url = request.get_data('image_url')
        body = request.form['body']
        author = request.form['author']
        quote = QuoteModel(body, author)
        path = meme.make_meme(temp_image, quote.body, quote.author)
        os.remove(temp_image)
    except requests.exceptions.RequestException:
        body = None
        author = None
        quote = QuoteModel(body, author)
        error_image = './_data/web_photos/musk_error.jpg'
        path = meme.make_meme(error_image, quote.body, quote.author)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
