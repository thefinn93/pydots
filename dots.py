#!/usr/bin/env python3

import random
import string

from flask import Flask
app = Flask(__name__)

LISTSIZE = random.randint(25, 100)
PATHSIZE = (10, 100)

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
    }


def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c, c) for c in text)


def genhtml(path=None):
    title = path
    if title is None:
        title = "..."
    html = "<html>\n<head>\n<title>%s</title>\n</head><body>" % title
    html += "<br />\n<code>\n<ul>"
    for i in range(0, LISTSIZE):
        length = random.randint(PATHSIZE[0], PATHSIZE[1])
        rand = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
        html += "<li><a href=\"/%s\">%s</a></li>\n" % (rand, rand)
    html += "</ul>\n</code>\n</body>\n</head>"
    return html


@app.route("/")
def index():
    return genhtml()


@app.route("/<path>")
def dots(path):
    return genhtml(html_escape(path))


@app.errorhandler(404)
def notfound(e):
    return genhtml(), 200


if __name__ == "__main__":
    app.run(debug=True)
