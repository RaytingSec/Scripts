# Create template notes txt file

import datetime

result = str(datetime.datetime.now().date()) + '\n'
result += '=' * 30 + '\n\n'
result += '## Sec1' + '\n\n'
result += '- note'

print(result)
