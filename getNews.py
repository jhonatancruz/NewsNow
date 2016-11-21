import bs4 as bs
import urllib.request

sauce= urllib.request.urlopen('https://www.tesla.com/blog').read()
soup= bs.BeautifulSoup(sauce,'lxml')

print("Top news:",soup.p.text) # returns top news in Tesla.com

# print(soup.get_text('div'))
# for div in soup.find_all('div',class_='post-info'):
#     print(div.text)
# for div2 in soup.find_all('div',class_='views-row-odd views-row-first blog-list-item'):
#     for div in soup.find_all('div',class_='post-info'):
#         for span in soup.find_all('span'):
#             print(span.string)
# for date in soup.find_all('span'):
#     print(date.string)
# print(soup.find_all('div',class_='post-info'))
# for url in soup.p.text():
#     print(soup.url)

print(soup.find_all('div',class_='views-row-odd views-row-first blog-list-item'))

for x in soup.find_all('div',class_='views-row-odd views-row-first blog-list-item'):
    for
