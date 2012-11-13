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
import json
import re
from bs4 import BeautifulSoup

def main():
    try:
        sites_file_raw = open('sites.json', mode='r').read()
        sites_no_comments = re.sub(r'//##.*', r'', sites_file_raw)
        sites = json.loads(sites_no_comments)
    except Exception, e:
        raise e
 
    for site in sites:
        print "Loading site: ", site['name']
        page = urllib2.urlopen(site['url']).read()
        print "Read ", len(page), " Bytes from page: ", site['url']
        soup = BeautifulSoup(page)
        for node_title in soup.findAll(site['node'], attrs = site['attrs']):
            print node_title.prettify()

if __name__ == '__main__':
    main()
