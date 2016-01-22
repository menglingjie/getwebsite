# -*- coding: utf-8 -*-

import urllib2
import bs4 as BeautifulSoup
import re
import gzip,StringIO
import os
import logging

logging.basicConfig(filename="log.txt",
                    format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %I:%M:%S %p',
                    level=logging.INFO)


def getHtmlString(response):
    html_str = response.read()
    if response.headers.has_key('content-encoding') and  response.headers['content-encoding']=='gzip' :
        pdata = StringIO.StringIO(html_str)
        gzipper = gzip.GzipFile(fileobj=pdata)
        html_str = gzipper.read()
    return html_str

def getlinks(host, url, html_str, pattern):
    links = []
    # 分析网页，找到所有的超链接，通过pattern过滤有效的超链接。
    soup = BeautifulSoup.BeautifulSoup(html_str,"html.parser")
    linksstring = soup.findAll(href=re.compile(pattern))
    for linkstring in linksstring :
        links.append(linkstring['href'])

    linksstring = soup.findAll(href=re.compile('^[^/]'))
    for linkstring in linksstring :
        if linkstring['href'].find('http') == -1 and linkstring['href'].find('javascript') == -1 :
            # relative path
            links.append(os.path.split(url)[0]+'/'+linkstring['href'])
        elif linkstring['href'].find('http://'+host) != -1:
            # match http://host
            if re.match(pattern, linkstring['href'][len('http://'+host):]) != None:
                # match http://host+pattern
                links.append(linkstring['href'][len('http://'+host):])

    logging.debug("Get %s links : %s", url, links)

    return links

def writehtmlfile(host, url, str):

    (path,filename) = os.path.split(host+url)
    if not os.path.exists(path):
        os.makedirs(path)
    with open(host+url,'w+') as f:
        logging.debug("Write html to : %s%s", host, url)
        f.write(str)

def fileDownloaded(host, url):
    ret = os.path.isfile(host+url)
    logging.debug("File %s exist? : %s", host+url, ret)
    return ret



def getHtmlFile(prot, host, url, pattern):
    if os.path.splitext(url)[1].find('#')==-1:
        logging.info("Get html : %s%s", host, url)
        print("Get html : %s%s"%(host,url))
        try:
            request = urllib2.Request(prot+host+url)
            response = urllib2.urlopen(request)

            html_str = getHtmlString(response)

            writehtmlfile(host, url, html_str)

            links = getlinks(host, url, html_str, pattern)
            for link in links :
                if (not fileDownloaded(host, link)) :
                    getHtmlFile(prot, host, link, pattern)
        except BaseException as e:
            logging.error("Error : %s", e)
            print("Error : %s"%e)


def getWebSite(args):
    getHtmlFile(args[0],args[1],args[2],args[3])

#getHtmlFile("http://", "www.runoob.com","/python/python-tutorial.html","^/python")
