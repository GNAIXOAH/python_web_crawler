from lxml import etree
from lxml import html
import requests
from bs4 import BeautifulSoup

r = requests.get("http://quotes.toscrape.com")

html = html.fromstring(r.text)
parser =etree.HTMLParser(encoding = "utf-8")
tree = etree.parse("http://quotes.toscrape.com", parser = parser)

sentence_path = html.xpath("//div[@class='container']/div[@class='row']/div[@class='col-md-8']/div[@class='quote']/span[@class='text']")
author_path = html.xpath("//div[@class='container']/div[@class='row']/div[@class='col-md-8']/div[@class='quote']/span/small[@class='author']")

sentences = []
authors = []
for sentence in sentence_path:
    sentences.append(sentence.text)
for author in author_path:
    authors.append(author.text)
for i in range(len(sentences)):
    print(sentences[i] + " by " + authors[i])

soup = BeautifulSoup(r.text, features="lxml")
sentences = []
authors = []

for sentence in soup.find_all(attrs={"class": "text"}):
    sentences.append(sentence.get_text())
for author in soup.find_all(attrs={"class": "author"}):
    authors.append(author.get_text())
for i in range(len(sentences)):
    print(sentences[i] + " by " + authors[i])