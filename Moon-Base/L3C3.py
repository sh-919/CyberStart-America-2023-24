import urllib.request, urllib.error, urllib.parse

response = urllib.request.urlopen("http://127.0.0.1:8080/winning")
html = response.read()
print(html)
