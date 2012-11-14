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
            sites = json.loads(sites_file.read())
            sites_file.close()
    except Exception, e:
        raise e

    for site in sites:
        print "Loading site: ", site['name']
        page = urllib2.urlopen(site['url']).read()

        print "Read ", len(page), " Bytes from page: ", site['url']

        try:
            page_dom = html.fromstring(page)

            for node in page_dom.xpath(site['node']):
                # a group of nodes, each contains a publication
                # xpath expression can be checked through various tools
                # e.g. the 'xpath check addon in firefox'

                # in some cases, these strings are broken into pieces
                node_title_raw = node.xpath(site['title'])
                # need to deal with nodes which lack some information
                node_title_full = ''
                for node_title_part in node_title_raw:
                    node_title_full += node_title_part
                # translate linefeed into spaces, merge multiple lines
                node_title = ' '.join(node_title_full.split())
                print "[TITLE] ", node_title.encode("utf-8")

                # same as above, working on author information
                node_author_raw = node.xpath(site['author'])
                node_author_full = ''
                for node_author_part in node_author_raw:
                    node_author_full += node_author_part
                node_author = ' '.join(node_author_full.split())
                print "[AUTHOR]", node_author.encode("utf-8"), '\n'

        except Exception, e:
            raise e

if __name__ == '__main__':
    main()
