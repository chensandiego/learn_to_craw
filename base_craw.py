import threading
import queue
from crawler import *
from CheckableQueue import *


THREAD_COUNT = 20

linksToCrawl=CheckableQueue()


def createCrawlers():
    for i in range(THREAD_COUNT):
        t=threading.Thread(target=run)
        t.daemon=True
        t.start()


def run():
    while True:
        url=linksToCrawl.get()
        try:
            if url is None:
                break
            Crawler.crawl(threading.current_thread(),url,linksToCrawl)
        except:
            print("Exception")
        linksToCrawl.task_done()


def main():
    url=input("Website>")
    Crawler(url)
    linksToCrawl.put(url)
    createCrawlers()
    linksToCrawl.join()
    print("total links crawled:{}".format(len(Crawler.crawledLinks)))
    print("total errors:{}".format(len(Crawler.errorLinks)))


if __name__=='__main__':
    main()
    
