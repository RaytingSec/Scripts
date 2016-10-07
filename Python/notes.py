#!/usr/bin/python3
# Create template notes txt file

import datetime
from subprocess import call
import sys

title = ""
ext = "md"
if len(sys.argv) > 1:
    title = sys.argv[1]

date = str(datetime.datetime.now().date())

result = date + '\n'
if len(sys.argv) > 1:
    result += title + '\n'
result += '=' * 30 + '\n\n'
result += '## '

filename = "{}".format(date)
if len(sys.argv) > 1:
    filename = "{} {}".format(date, title)
filename += "." + ext

with open(filename, "w") as file:
    file.write(result)

call(["subl", filename])
