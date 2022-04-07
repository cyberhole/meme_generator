"""Joints together the image and text to make the meme."""
from PIL import Image, ImageDraw, ImageFont
import random
from QuoteEngine import QuoteModel


class MemeEngine:
    """Create a Meme With a Text and an Author."""

    def __init__(self, output_dir='./static'):
        """Construct the image path for the meme."""
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500):
        """Make a meme, takes the image path, text and author."""
        img_path
        img = Image.open(img_path)

        output_dir = './static/1.jpg'
        y = random.randint(20, 460)

        if width is not None:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        if text is not None and author is None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./_data/fonts/LilitaOne-Regular.ttf',
                                      size=20)
            draw.text((20, y), text, font=font, fill='white')

        if author is not None and text is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./_data/fonts/LilitaOne-Regular.ttf',
                                      size=20)
            draw.text((20, y),
                      repr(QuoteModel(text, author)),
                      font=font,
                      fill='white')

        img.save(output_dir)
        return output_dir
