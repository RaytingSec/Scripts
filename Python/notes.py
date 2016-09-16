# Create template notes txt file

import datetime
from subprocess import call

date = str(datetime.datetime.now().date())

result = date + '\n'
result += '=' * 30 + '\n\n'
result += '## '

filename = "{}.md".format(date)

with open(filename, "w") as file:
    file.write(result)

call(["subl", filename])
