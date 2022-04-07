# Intermediate Python Nanodegree Program: MEME GENERATOR

This is the project for the second course in the [Udacity Intermediate Python Nanodegree Program]: Meme Generator.

<img src="_data/readme.jpg"/>

The meme generator as the name says creates memes. There is a folder in _data/photos with the name dogs that is used as the meme default pictures.
This project can be used in two ways. One is by using args to define the path to a local image and then adding the text and author on top of the photo.
The second way is by executing a web page and then generate a random meme or creating a new one using a link of a photo with your text.

## Dependencies for Running Locally
* flask: [pip install flask -U]
* requests: [pip install requests]
* setuptools: [pip install -U setuptools]
* python-docx: [pip install python-docx]
* pandas: [pip install pandas]


## Basic Build Instructions 
# Generating the web page:
1. python3 app.py
2. Open http://127.0.0.1:5000

# Indicating the local path to the folder
1. python meme.py --path=<insert your path here> 
                   --body<insert your text here> 
                   --author<say your name here>
2. Meme will be saved at: ./static with the name 1.jpg
