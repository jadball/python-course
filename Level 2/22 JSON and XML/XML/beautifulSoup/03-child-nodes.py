from bs4 import BeautifulSoup

from ReadFile import readFile

doc = readFile("xml/book.xml")
soup = BeautifulSoup(doc, features='html5lib')

print("<book> has", len(soup.book), "child nodes")

i = 0
for child in soup.book:
    i = i + 1
    print(i, ":", child)
1
