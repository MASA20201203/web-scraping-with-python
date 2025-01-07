"""ch01 p5 first scraping file"""

from urllib.request import urlopen

html = urlopen("http://www.pythonscraping.com/pages/page1.html")
print(html.read())
