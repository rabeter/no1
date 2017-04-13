from bs4 import BeautifulSoup as bs
import requests as re

demo = re.get("https://github.com/rabeter/no1")
demo = demo.text
sope = bs(demo)

for link in sope("a"):
    print(link.get("href"))