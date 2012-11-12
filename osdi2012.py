#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ShiZhan
#
# Created:     13/11/2012
# Copyright:   (c) ShiZhan 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import urllib2
from bs4 import BeautifulSoup

def main():
    url_osdi_2012 = "http://www.usenix.org/conference/osdi12/tech-schedule/osdi-12-program"
    page = urllib2.urlopen(url_osdi_2012).read()
    print "Read page: ", len(page), " Bytes."
    soup = BeautifulSoup(page)
    for node_title in soup.findAll('h2', attrs={'class': 'node-title clearfix'}):
        print node_title
        pass

if __name__ == '__main__':
    main()
