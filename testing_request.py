from requests_html import HTMLSession
from requests_html import AsyncHTMLSession
from bs4 import BeautifulSoup as bs

url = "https://www.computer.org/csdl/journals"

session = HTMLSession()
r = session.get(url)

r.html.render(sleep=1)
print(bs(r.content, 'html.parser'))

