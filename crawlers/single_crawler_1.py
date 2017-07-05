
import requests
import re
from pyquery import PyQuery as pq

baseUrl = 'https://www.qiushibaike.com/8hr/page/{}/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }


class CacheDict(dict):
    def __init__(self,length=3):
        dict.__init__(self)
        self._length = length
        
    def __setitem__(self,key,value):
        dict.__setitem__(self,key,value)
        if len(self) > self._length:
            #print((list(self.keys()))[0])
            self.pop(list(self.keys())[0])
            
            
class QSBK(object):
    def __init__(self):
        self._cache = CacheDict(5)
        
            
    def getPageCode(self,pageIndex):
        cache_content = self._cache.get(pageIndex,None)
        if cache_content:
            return cache_content
        url = baseUrl.format(pageIndex)
        res = requests.get(url,headers=headers)
        ctt = pq(res.text)
        pardivs = pq('div.article.block',ctt)
        pages = CacheDict(5)
        pageItems = []
        for pardiv in pardivs:
            pageItem = {}
            pageItem['content'] = pq(pardiv).find('div.content span').text()
            pageItem['stars'] = pq(pardiv).find('div.stats span.stats-vote i.number').text()
            pageItems.append(pageItem)
        self._cache[pageIndex] = pageItems
        return pageItems;
    
    
    def formatPrint(self,items):
        for item in items:
            print('=============================================\n')
            print(item['content'])
            print('\n')
            print('stars:{}'.format(item['stars']))
            print('\n')
        print('press enter to next page\n')
    
        
def main():
    qsbk = QSBK()
    shift = True
    index = 1
    while shift:
        items = qsbk.getPageCode(index)
        qsbk.formatPrint(items)
        key = input()
        if key.upper() != 'Q':
            index += 1
        else:
            shift = False
        
            
            
if __name__ == '__main__':
    main()
    