import time
import requests
import wordsmaker
import sys
import createimg
from Queue import Queue
import threading

class chartDivider:
    def __init__(self):
        self.letters = []
        self.numbers = []
        self.hash = 0
        self.state = 1

    def gethash(self):
        r = requests.get('http://moneroblocks.info/api/get_stats/').json()
        hr = requests.get('http://moneroblocks.info/api/get_block_header/{0}'.format(r['height'])).json()
        mhash = hr['block_header']['hash']
        if mhash != self.hash:
            self.hash = mhash
            self.isolate()
            self.state = 1
        else:
            self.state = 0

    def isolate(self):
        self.letters = ''
        self.numbers = []
        for c in self.hash:
            if c.isdigit():
                self.numbers.append(c)
            else:
                self.letters += c


    def createword(self):
        rr = wordsmaker.run(str(self.letters))
        self.search_keyword = rr[0]

    def download_page(self, url):
        version = (3, 0)
        cur_version = sys.version_info
        if cur_version >= version:  # If the Current Version of Python is 3.0 or above
            import urllib.request  # urllib library for Extracting web pages
            try:
                headers = {}
                headers[
                    'User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                req = urllib.request.Request(url, headers=headers)
                resp = urllib.request.urlopen(req)
                respData = str(resp.read())
                return respData
            except Exception as e:
                print(str(e))
        else:  # If the Current Version of Python is 2.x
            import urllib2
            try:
                headers = {}
                headers[
                    'User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
                req = urllib2.Request(url, headers=headers)
                response = urllib2.urlopen(req)
                page = response.read()
                return page
            except:
                return "Page Not found"

    # Finding 'Next Image' from the given raw page
    def _images_get_next_item(self, s):
        start_line = s.find('rg_di')
        if start_line == -1:  # If no links are found then give an error!
            end_quote = 0
            link = "no_links"
            return link, end_quote
        else:
            start_line = s.find('"class="rg_meta"')
            start_content = s.find('"ou"', start_line + 1)
            end_content = s.find(',"ow"', start_content + 1)
            content_raw = str(s[start_content + 6:end_content - 1])
            return content_raw, end_content

    # Getting all links with the help of '_images_get_next_image'
    def _images_get_all_items(self, page):
        items = []
        while True:
            item, end_content = self._images_get_next_item(page)
            if item == "no_links":
                break
            else:
                items.append(item)  # Append all the links in the list named 'Links'
                time.sleep(0.1)  # Timer could be used to slow down the request for image downloads
                page = page[end_content:]
        return items

    def run(self):
        self.gethash()
        img_links = []
        if self.state == 1:
            self.createword()
            search = self.search_keyword.replace(' ', '%20')
            url = 'https://www.google.com/search?q=' + search + '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
            raw_html = (self.download_page(url))
            time.sleep(0.1)
            img_links = img_links + (self._images_get_all_items(raw_html))
        if len(img_links) > 0:
            return img_links
        else:
            return None


def creat(i):
    p = createimg.polyline(numbers, i)

def workerddl():
    item = q.get()
    creat(item)
    q.task_done()


chart = chartDivider()
imgs = chart.run()
numbers = chart.numbers
q = Queue()
for i in range(len(imgs)):
    t = threading.Thread(target=workerddl)
    t.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
    t.start()
for i in imgs:
    q.put(i)
q.join()