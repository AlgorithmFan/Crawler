#!usr/bin/env python
#coding: utf-8

import urllib2
import gzip
import StringIO


class Crawler:
    def __init__(self):
        self.req_header =  {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                  'Accept':'text/html;q=0.9,*/*;q=0.8',
                  'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                  'Accept-Encoding':'gzip',
                  'Connection':'close',
                  'Referer':'http://csis.org/' #注意如果依然不能抓取的话，这里可以设置抓取网站的host
                  }
        self.req_timeout = 60


    def getSourceCode(self, url):
        try:
            req = urllib2.Request(url, None, self.req_header)
            resp = urllib2.urlopen(req, None, self.req_timeout)
            html = resp.read()#.decode('utf-8')
            compressStream = StringIO.StringIO(html)
            gzipper = gzip.GzipFile(fileobj=compressStream)
            html = gzipper.read()
            resp.close()
        except:
            #print 'Wrong:\t', url
            html = ''
        return html




if __name__ == '__main__':
    url = 'http://www.defensenews.com/story/defense/show-daily/space-symposium/2016/04/12/us-uae-share-space-situational-awareness-data/82936792/'
    crawler = Crawler()
    html = crawler.getSourceCode(url)

    fp = open('text.html', 'w')
    fp.write(html)
    fp.close()
