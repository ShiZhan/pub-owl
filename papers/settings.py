# Scrapy settings for papers project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'papers'

SPIDER_MODULES = ['papers.spiders']
NEWSPIDER_MODULE = 'papers.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'papers (+http://www.yourdomain.com)'
