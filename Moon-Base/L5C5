import urllib.request, urllib.parse, urllib.error

data = urllib.parse.urlencode({"user":"tweetbotuser","status-update":"alientest"})
data = data.encode("ascii")
url = "http://127.0.0.1:8082"


req = urllib.request.Request(url, headers={"x-api-key":"tweetbotkeyv1"}, data=data)


response = urllib.request.urlopen(req)
print(response.read())
