from bs4 import BeautifulSoup

from ReadFile import readFile

doc = readFile("xml/book.xml")
soup = BeautifulSoup(''.join(doc), features='html5lib')
print(soup.prettify())
