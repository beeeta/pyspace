
import requests
import re
from pyquery import PyQuery

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
        
    def getPage(self,pageIndex):
        url = baseUrl.format(pageIndex)
        itms = self.getPageCode(url)
            
    def getPageCode(self,url):
        res = requests.get(url,headers=headers)
        pq = PyQuery(res.text)
        pardiv = pq('')
        
        
        
            
if __name__ == '__main__':
    cd = CacheDict()
    for i in range(5):
        cd[i] = str(i)*2
    print(cd)