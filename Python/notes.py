# Create template notes txt file

import datetime

date = str(datetime.datetime.now().date())

result = date + '\n'
result += '=' * 30 + '\n\n'
result += '## '

with open(date, "w") as file:
    file.write(result)
