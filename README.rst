pub-owl
=======

data collector
--------------

A web crawler for collecting online academic publication metadata.

Based on scrapy_ framework, use :code:`pip install scrapy` to build up running environment.

spiders
^^^^^^^

Spiders for collecting academic publication metadata.

usenix
++++++

Collecting bibliography data from some selected `USENIX conferences`_.

usenix_proceedings
++++++++++++++++++

Collecting paper list from all `USENIX proceedings`_ since 1993. 

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
.. _`USENIX conferences`: https://www.usenix.org/conferences/past
.. _`USENIX proceedings`: https://www.usenix.org/publications/proceedings
