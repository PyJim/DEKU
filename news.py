import requests
from bs4 import BeautifulSoup

def getNews():
    url = 'https://www.bbc.com/news'
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')
    unwanted = ['BBC World News TV', 'BBC World Service Radio',
                'News daily newsletter', 'Mobile app', 'Get in touch']
    all_news = []
    for x in list(dict.fromkeys(headlines)):
        if x.text.strip() not in unwanted:
            all_news.append(x.text.strip())
    return all_news[:10]