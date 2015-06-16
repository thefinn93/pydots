#!/usr/bin/env python3

import random
import string

import dataset

from flask import Flask, request
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

db = dataset.connect('sqlite:///var/log/pydots/visitorlog.db')
visitorlog = db['hits']


def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c, c) for c in text)


def genhtml(path=None):
    visitorlog.insert(dict(remote_addr=request.remote_addr,
                           hostname=request.hostname,
                           referrer=request.referrer,
                           path=path,
                           useragent=request.headers.get('User-Agent')))
    title = path
    if title is None:
        title = "Hello, crawlers!"
    html = "<html>\n<head>\n<title>%s</title>\n</head><body>" % title
    html += "Dots, for crawlers that don't read the <a href=\"/robots.txt\">robots.txt</a>"
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


if __name__ == "__main__":
    app.run(debug=True)
