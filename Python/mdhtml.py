#!/usr/bin/python3
# Converts markdown to formatted html
# mdhtml.py readme.md -> readme.html

import sys
import os
from bs4 import BeautifulSoup as bsoup
import markdown

mdfile = sys.argv[1]
if not os.path.isfile(mdfile):
    sys.exit("File doesn't exist:\n" + mdfile)

with open(mdfile, 'r') as file:
    mdcontent = file.read()

md = markdown.Markdown(output_format='html5')
htmlcontent = md.convert(mdcontent)
htmlpretty = bsoup(htmlcontent, 'lxml').prettify()

htmlfile = os.path.splitext(mdfile)[0] + '.html'

with open(htmlfile, 'w') as file:
    file.write(htmlpretty)
