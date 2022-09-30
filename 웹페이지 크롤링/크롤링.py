from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://www.naver.com")
bsObject = BeautifulSoup(html, "html.parser")

