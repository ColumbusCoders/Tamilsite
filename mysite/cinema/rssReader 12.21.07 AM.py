from bs4 import BeautifulSoup
import feedparser

# define class object to hold parsed data fields
class rssresult(object):
    def __init__(self, title=None, link=None,published=None,img=None,summary=None,desc=None):
        self.title = title
        self.link = link
        self.published = published
        self.img = img
        self.summary = summary
        print desc
        self.desc = desc

# function that takes URLs are params, then parse and save it class of array
def GetParseResults(urls):
   resultList = []
   for i in urls:
      print i
      results = feedparser.parse(i)
      for x in results.entries:
         soup = BeautifulSoup(x.summary,'html.parser')
         images = soup.find('img')
         para = soup.find('<p>')
         src = images['src']
         print src
         resultList.append(rssresult(x.title,x.link,x.published,src,x.summary,para))
      print len(resultList)
   return resultList


#urls_1 = ["http://cinema.dinamalar.com/rss.php"]
#NewsFeed = GetParseResults(urls_1)
#entry = NewsFeed.entries[0]
# print entry.keys()
