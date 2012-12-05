pub-owl.collector
=======

data collector
------

A web crawler for collecting online academic publication metadata.

Crawler based on [scrapy](https://github.com/scrapy/scrapy) framework.

rdf adapter
------

Translates crawled data into pub-owl ontology as instances.

Work with collected data, convert to [W3C Resource Description Framework (RDF)](http://www.w3.org/RDF/) model by using [rdflib](https://github.com/RDFLib/rdflib) and [FOAF](http://xmlns.com/foaf/spec/) specification.

