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
#!/usr/bin/python
#coding=utf-8

import optparse
import urllib2
import json
import re
from lxml import html

def main():
    option_parser = optparse.OptionParser("usage: %prog [-S <sitesfile>]")
    option_parser.add_option("-S", "--sites", dest="sitesfile",
        default="sites.json", type="string",
        help="specify sites.json file to run on")

    (options, args) = option_parser.parse_args()
    if len(args) > 1:
        option_parser.error("incorrect number of arguments")

    sitesfile = options.sitesfile

    try:
        with open(sitesfile, mode='r') as sites_file:
            sites_no_comments = re.sub(r'//##.*', r'', sites_file.read())
            sites = json.loads(sites_no_comments)
            sites_file.close()
    except Exception, e:
        raise e

    for site in sites:
        print "Loading site: ", site['name']
        page = urllib2.urlopen(site['url']).read()

        print "Read ", len(page), " Bytes from page: ", site['url']

        try:
            page_dom = html.fromstring(page)
            for node_title in page_dom.xpath(site['node']):
                print node_title.encode("utf-8")
        except Exception, e:
            raise e

if __name__ == '__main__':
    main()
