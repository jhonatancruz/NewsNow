import bs4 as bs
import urllib.request
import requests
from twilio import twiml
from twilio.rest import TwilioRestClient
from bs4 import BeautifulSoup

def news(company):
    URL ='https://news.google.com/news/search/section/q/'+company+'/'+company+'?hl=en&gl=US&ned=us'
    response= requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    most_recent_news= soup.find_all("a", { "class" : "nuEeue hzdq5d ME7ew" })
    news={"headlines":[], "urls":[] }
    for moreNews in most_recent_news:
        news['headlines'].append(moreNews.text)
        news['urls'].append(moreNews.get('href'))
    return(news)
    # print("News:",news["headlines"][0].strip(),"\n","Url:",news["urls"][0].strip())
