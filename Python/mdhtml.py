#!/usr/bin/python3
# Converts markdown to formatted html
# mdhtml.py readme.md -> readme.html

import sys
import os
from bs4 import BeautifulSoup as bsoup
import markdown

# File argument
file_md = sys.argv[1]
if not os.path.isfile(file_md):
    sys.exit("File doesn't exist:\n" + file_md)

with open(file_md, 'r') as file:
    content_md = file.read()

# Process content
content_html = bsoup(markdown.markdown(content_md), 'lxml').prettify()
content_html += '\n'  # EOF newline
file_html = os.path.splitext(file_md)[0] + '.html'

with open(file_html, 'w') as file:
    file.write(content_html)
