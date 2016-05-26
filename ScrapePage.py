import urllib
sock = urllib.urlopen("http://www.opentable.com/perbacco-san-francisco")
htmlSource = sock.read()
sock.close()
print htmlSource
