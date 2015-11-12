author__ = 'jeffrey'
from bs4 import BeautifulSoup
import requests
import re
print('hello');

seeds = ['http://is.njit.edu']
njit = 'http://is.njit.edu'
queued = []

def getdata(s):
    source = requests.get(s)
    soup = BeautifulSoup(source.text, "html.parser")
    for link in soup.findAll('a'):
        links = (link.get('href'))
        links = str(links)  # print('Downloading Link', links)
        if links.startswith('/'):
            queued.append(njit+links)
        if 'http://is.' in links and 'njit' in links:
            queued.append(links)
    return queued


GoodUrls = []
badUrl = []
Crawled = []

def download(url):
    global Crawled
    good = open("goodURLs.txt", "w")
    CSV = {}

    if getdata(url).pop(0) not in badUrl:
        for w in getdata(getdata(url).pop(0)):
            source = requests.get(w)
            soup = BeautifulSoup(source.text,"html.parser")
            for images in soup.findAll('img'): # search for images
                image = (images.get('src'))
                image = str(image)
                print(image)

            for links in soup.findAll('a'): # search for links and pdf files.
                link = (links.get('href'))
                link = str(link)
                print(link)

                if "http://is." in links and links.endswith('.php') and w not in Crawled:

                    seeds.extend([w])
                    #print(links)
                    Crawled.append(links)
                if "http://is." in links and w not in Crawled:
                    pass
                    print(links)
                #if "http://is." in links:

                    #print(links)

                    #if links.endswith('.php') and w not in Crawled:
                      #  print(links)


                   # print(links)
                        #rawled.append(w)
                        #print('this is the w', w)
                        #print('this is the ', links)
                        #seeds.extend([w])
                    #else:
                     #   print(w)
                      #  badUrl.append(links)
def main(url):
    while True:
        for seed in url:
            download(seed)
main(seeds)
