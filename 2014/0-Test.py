from urllib2 import urlopen
html = urlopen("http://cl.ddder.us/htm_data/7/1706/2454220.html")
print(html.read())