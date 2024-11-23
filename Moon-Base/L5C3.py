import zipfile
import itertools
import time

def extractFile(zfile, password):
  try:
    zfile.extractall("/tmp", pwd=password)
    return True
  except:
    return False

zipfile = zipfile.ZipFile("/tmp/alien-zip-2092.zip")
digits = "0123456789"

for c in itertools.product(digits, repeat=3):
  s = ''.join(str(x) for x in c)
  print("Trying: " + str(s))
  
  if extractFile(zipfile, str.encode(s)):
    print("Code found!: " + str(s))
    break

txtfile = open("/tmp/alien-zip-2092.txt", "r")
contents = txtfile.read()
print(contents)
txtfile.close()
