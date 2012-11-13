#-------------------------------------------------------------------------------
# Name:        publication crawler
# Purpose:     grab info from various publication web
#
# Author:      ShiZhan
#
# Created:     13/11/2012
# Copyright:   (c) ShiZhan 2012
# Licence:     MIT
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import urllib2
from bs4 import BeautifulSoup

sites = [
    {
        'name' : 'OSDI 2012', # use local page for test
        # 'url' : "https://www.usenix.org/conference/osdi12/tech-schedule/osdi-12-program",
        'url' : "file:///E:/Works/hive/pub-owl.collector/.testpage/osdi2012.htm",
        'node' : 'h2',
        'attrs' : {'class' : 'node-title clearfix'},
    },
    {
        'name' : 'WWW 2011',
        # 'url' : "http://www.www2011india.com/proceeding/forms/pcontents.htm",
        'url' : "file:///e:/Works/hive/pub-owl.collector/.testpage/www2011.htm",
        'node' : 'font',
        'attrs' : {'color' : '#177EB9', 'face' : 'Arial', 'size' : '2'}
    },
    {
        'name' : 'SOSP 2011',
        # 'url' : "http://sigops.org/sosp/sosp11/current/index.html",
        'url' : "file:///E:/Works/hive/pub-owl.collector/.testpage/sosp2011.html",
        'node' : 'div',
        'attrs' : {'class' : 'paperTitle'}
    }
]

def main():
    for site in sites:
        print "Loading site: ", site['name']
        page = urllib2.urlopen(site['url']).read()
        print "Read ", len(page), " Bytes from page: ", site['url']
        soup = BeautifulSoup(page)
        for node_title in soup.findAll(site['node'], attrs = site['attrs']):
            print node_title

if __name__ == '__main__':
    main()
