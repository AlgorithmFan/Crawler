#!usr/bin/env python
#coding: utf-8


from Crawler import Crawler
from util import MySQLDatabase
from BeautifulSoup import BeautifulSoup

class DefenseCrawler(Crawler):
    def __init__(self, filename):
        Crawler.__init__(self)
        self.viewed_url = set()   # store the href with hash value
        self.candidate_url = list()
        self.database = self.connectDb()

    def connectDb(self):
        ip = 'localhost'
        user = 'root'
        password = '123456'
        database = 'baidu'
        db = MySQLDatabase(ip, user, password, database)
        db.OpenDb()
        return db

    def iterative(self, url):
        urlhash = hash(url)
        if urlhash in self.viewed_url:
            return False
        self.viewed_url.add(urlhash)

        html = self.getSourceCode(url)
        values = [(url, html)]

        insertSQL = 'insert into defenceNews(url, content) values(%s, %s)'
        self.database.InsertTb(insertSQL, values)

        hrefs = self.getHref(html)
        for href in hrefs:
            if href.startswith('/'):
                href = url[:-1] + href
            urlhash = hash(href)
            if urlhash in self.viewed_url:
                continue
            self.candidate_url.append(href)
        return True

    def getHref(self, html):
        ''''''
        soup = BeautifulSoup(html)
        results = soup.findAll("a", href=True)
        urls = set()
        for item in results:
            urls.add(item['href'])
        return urls

    def run(self, url):
        self.candidate_url.append(url)
        num = 0
        logger = open('url.txt', 'w')
        while len(self.candidate_url):
            try:
                if self.candidate_url[0].find('defensenews') == -1:
                    print 'NoCrawling: {url}'.format(url = self.candidate_url[0])
                else:
                    print '{num}\tCrawling: {url}'.format(num=num, url = self.candidate_url[0])
                    if self.iterative(self.candidate_url[0]):
                        num += 1
                del self.candidate_url[0]
            except:
                # logger.write(self.candidate_url[0] + '\n')
                del self.candidate_url[0]
        self.database.CloseDb()

if __name__ == '__main__':
    url = 'http://www.defensenews.com/'

    filename = 'defense.csv'
    dfCrawler = DefenseCrawler(filename)
    dfCrawler.run(url)
