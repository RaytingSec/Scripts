# Create template notes txt file

import datetime

date = str(datetime.datetime.now().date())

result = date + '\n'
result += '=' * 30 + '\n\n'
result += '## Section 1' + '\n\n'
result += ('- Bullet' + '\n') * 3

with open(date, "w") as file:
    file.write(result)
