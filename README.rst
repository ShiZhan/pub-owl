pub-owl
=======

data collector
--------------

A web crawler for collecting online academic publication metadata.

Crawler based on scrapy_ framework.

rdf adapter
-----------

Translates crawled data into pub-owl ontology as instances.

Work with collected data, convert to W3C Resource Description Framework (RDF_) model by using rdflib_ and FOAF_ specification.

front end
---------

...

.. _scrapy: https://github.com/scrapy/scrapy
.. _RDF: http://www.w3.org/RDF/
.. _rdflib: https://github.com/RDFLib/rdflib
.. _FOAF: http://xmlns.com/foaf/spec/
