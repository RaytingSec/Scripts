#!/usr/bin/python3

import datetime
import subprocess
import sys

h = """General purpose markdown generator for date-sensitive notes
\tUsage: notes [title]
"""

if len(sys.argv) > 2:
    print(h)
    sys.exit('Too many parameters!')
elif len(sys.argv) == 2:
    title = sys.argv[1]
else:
    title = ''


date = datetime.date.today().isoformat()
result = date + '\n'
if title:
    result += title + '\n'

# result += '=' * 30 + '\n\n'
# result += '## '

result += """==============================

## 
"""

if title:
    filename = '{} {}'.format(date, title)
else:
    filename = date

filename += '.md'

with open(filename, 'w') as file:
    file.write(result)

subprocess.call(['subl', filename])
