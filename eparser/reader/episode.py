from bs4 import BeautifulSoup
import requests


def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    fp = requests.get(url, headers=headers)
    mybytes = fp.content

    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr

def all_ep_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    block = soup.find('div',{'class':"starMovieAndTvplay"})
    listItem = block.findAll('li', {'class':'listItem'})
    return listItem

def Title(item):
    return item.find('b', {'class':'title'}).text

root = 'https://baike.baidu.com'

def GetURL(item):
    addr = item.find('b', {'class':'title'})
    try:
        url = addr.a['href']
        return root + url
    except:
        return None

def RemoveSup(item):
    for sup in item.find_all('sup'):
        sup.replaceWith('')
    return item

def CharacterName(item):
    item = RemoveSup(item)
    keys = item.dl.findAll('dt')
    values = item.dl.findAll('dd')
    dic = {k.text:v.text for k,v in zip(keys, values)}
    if '饰演' in dic:
        name = dic['饰演']
    else:
        name = None
    
    return name

def Year(item):
    year = item.find('b', {'class':'title'}).find_next_sibling().text
    return year

def ItemInfo(item):
    info = {'name':CharacterName(item), 'url':GetURL(item), 'title':Title(item), 'year':Year(item)}
    return info


class EpisodeList:
    def __init__(self, actress:str):
        self.actress = actress
        self.html = get_html(actress)
        self.all_eps = all_ep_html(self.html)
        self.elist = list(map(ItemInfo, self.all_eps))
    
    def __call__(self):
        return self.elist
    
    def __repr__(self):
        return str(self.elist)