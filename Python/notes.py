# Create template notes txt file

import datetime
from subprocess import call
import sys

if len(sys.argv) > 1:
    title = sys.argv[1]
else:
    title = ""

date = str(datetime.datetime.now().date())

result = "{}\n{}\n".format(date, title)
result += '=' * 30 + '\n\n'
result += '## '

filename = "{} {}".format(date, title)

with open(filename, "w") as file:
    file.write(result)

call(["subl", filename])
