import requests
from pyquery import PyQuery as pq
import time

base_url = 'https://tieba.baidu.com/p/{}?see_lz={}'

class BDZD(object):
    def __init__(self,topicId,seeLz=1):
        self.topicId = topicId
        self.seeLz = seeLz
        self.url = base_url.format(self.topicId,self.seeLz)
        self.currentPageNum = 1
        self.currentPageContent = ''
        self.totalPage = 1
        
    def geneCurrentPage(self):
        def formatStr(src,width=40):
            index = 1
            while index*width<len(src):
                src = src[:index*width] + '\n' + src[index*width:]
                index += 1
            return src
        
        url = self.url + "&pn=" + str(self.currentPageNum)
        r = requests.get(url)
        divs = pq(r.text).find('div.d_post_content.j_d_post_content')
        index = 1
        self.currentPageContent = ''
        self.currentPageContent += '\n**********************第{}页**********************\n'.format(self.currentPageNum)
        for i in divs.items():
            self.currentPageContent += '\n======================第{}楼======================\n'.format(index)
            self.currentPageContent += formatStr(i.text())
            index += 1
        
    def saveToFile(self,fileName):
        with open(fileName,'a') as f:
            print('正在保存第{}页'.format(self.currentPageNum))
            f.write(self.currentPageContent)
        
    def initPageCount(self):
        url = self.url + "&pn=1"
        r = requests.get(url)
        count = pq(r.text).find('div.l_thread_info li.l_reply_num span.red').eq(1).text()       
        self.totalPage = count
        
    def main(self):
        self.initPageCount()
        print('总页数为：{}'.format(self.totalPage))
        for i in range(int(self.totalPage)):
            self.geneCurrentPage()
            self.saveToFile(str(self.topicId)+'_' + time.strftime('%Y-%m-%d')+ '.txt')
            self.currentPageNum += 1
        
    
if __name__ == '__main__':
    bdzd = BDZD(3138733512)
    bdzd.main()
