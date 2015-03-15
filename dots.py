#!/usr/bin/env python3

import random
import string

from flask import Flask
app = Flask(__name__)

LISTSIZE = 50
DOTSLENGTH = 50


def genhtml(path=None):
    title = path
    if title is None:
        title = "Hello, crawlers!"
    html = "<html>\n<head>\n<title>%s</title>\n</head><body>" % title
    html += "Dots, for crawlers that don't read the <a href=\"/robots.txt\">robots.txt</a>"
    html += "<br /><ul>"
    for i in range(0, LISTSIZE):
        rand = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(DOTSLENGTH))
        html += "<li><a href=\"/dots/%s\">%s</a></li>" % (rand, rand)
    html += "</ul>\n</body>\n</head>"
    return html


@app.route("/dots/")
def index():
    return genhtml()


@app.route("/dots/<path>")
def dots(path):
    return genhtml(path)


if __name__ == "__main__":
    app.run(debug=True)
