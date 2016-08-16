import requests
import ssl
from bs4 import BeautifulSoup
import os
import getpass

# For SSL compatibility
class SSL_adapter(requests.adapters.HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = requests.packages.urllib3.poolmanager.PoolManager(num_pools=connections, maxsize=maxsize, block=block, ssl_version=ssl.PROTOCOL_TLSv1)

user = input("username: ")
passwd = getpass.getpass("password: ")
auth = (user, passwd)

# Login 1

domain = "https://REDACTED"

s = requests.Session()
s.mount('https://', SSL_adapter())
r = s.get(domain, auth = auth)
if r.status_code == 200:
    print("Authenticated to main site")

# Login 2

loginpage = domain + "/_layouts/ens/Login.aspx?ReturnUrl=/_layouts/ens/advices.aspx"
advices = domain + "/_layouts/ens/advices.aspx"

r = s.get(loginpage)
# Scrape all input fields
data = {e['name']: e.get('value', '') for e in BeautifulSoup(r.text, "lxml").findAll('input', {'name': True})}
# input passwd
data['ctl00$PlaceHolderMain$txtPassword'] = passwd
r = s.post(loginpage, data)
confirm = s.get(loginpage)

fail = "File Not Found"
validated = "already validated"
if validated in confirm.text:
    print("Passed second authentication")
elif fail in confirm.text:
    print("Probably not authenticated")
else:
    print("Couldn't identify page")

# Get PDFs

tags = BeautifulSoup(r.text, "lxmlclear").findAll('tr')
parsed = []
for tr in tags:
    val = tr.findAll('td')[0].string
    if val is not None:
        val = val[:len(val)-1] # remove trailing period
        if val.isdecimal():
            # save tuple with date and url for pdf
            a = tr.findAll('td')[3].string.split('/')
            date = a[2] + '-' + a[0] + '-' + a[1]
            url = tr.findAll('a')[0].get('href')
            parsed.append((date, url))

# Downloading magic
counter = 0
url_base = domain + "/_layouts/ens/"
for a in parsed:
    counter += 1
    name = a[0] + " SFUSD.pdf"
    url_full = url_base + a[1]
    print("{} ({}/{}) ...".format(name, counter, len(parsed)))
    # Handle name collisions
    if (os.path.exists(name)):
        n = 0
        newName = name
        while (os.path.exists(newName)):
            n +=1
            newName = "{}.{}".format(name, n)
        print("{} exists, saving as {}".format(name, newName))
        finalName = newName
    else:
        finalName = name
    # Download
    # with open(finalName, "wb") as file:
    #     response = s.get(url_full)
    #     file.write(response.content)

print("Done")
