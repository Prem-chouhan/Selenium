import requests
content_type = requests.head('http://www.python.org').headers['content-type']
print(content_type)


import requests

content_type =requests.head()