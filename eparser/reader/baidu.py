from bs4 import BeautifulSoup
import requests


def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    fp = requests.get(url, headers=headers)
    mybytes = fp.content

    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr

def get_titles(html):
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.findAll(name='ul', attrs={'class':'dramaSerialList'})[0].findAll('span')
    titles = [f'[{i+1}/{len(titles)}]'+s.text for i, s in enumerate(titles)]
    return titles

def get_contents(html):
    soup = BeautifulSoup(html, 'html.parser')
    contents = soup.findAll(name='ul', attrs={'class':'dramaSerialList'})[0].findAll('dd')
    if len(contents) == 0:
        contents = soup.findAll(name='ul', attrs={'class':'dramaSerialList'})[0].findAll('p')
    contents = [s.text.replace('\n', '') for s in contents]
    return contents

def get_series(html):
    try:
        series = {title:content for title, content in zip(get_titles(html), get_contents(html))}
    except:
        raise ValueError('No content found!')
    return series

def clean_string(s):
    s = s.replace('\u3000', '')
    return s

def _search_sentence(s, key):
    slist = s.split('。')
    slist = list(filter(lambda x:(x.count(key)>0), slist))
    slist = list(map(clean_string, slist))
    return slist

def search(series, key):
    return {k:_search_sentence(series[k], key) for k in series}


class baidu_reader:
    def __init__(self, url):
        self.html = get_html(url)
        self.series = get_series(self.html)
    
    def search(self, key):
        result = search(self.series, key)
        return {k:result[k] for k in filter(lambda k: len(result[k])>0, result)}