# Send a spoofed email.  Use smtp server at '127.0.0.1', port 1025.
# Author needs to be bob-roswell-1947@gmail.com
# Recipient needs to be zultron@thebigeye.com


import smtplib

port = 1025
host = '127.0.0.1'
sender = "bob-roswell-1947@gmail.com"
recipent = "zultron@thebigeye.com"

s = smtplib.SMTP(host=host,port=port)
s.sendmail(from_addr=sender,to_addrs=recipent, msg="Hello.")
