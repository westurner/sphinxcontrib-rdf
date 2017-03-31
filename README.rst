===============================
sphinxcontrib-rdf
===============================

.. image:: https://badge.fury.io/py/sphinxcontrib-rdf.png
    :target: http://badge.fury.io/py/sphinxcontrib-rdf
    
.. image:: https://travis-ci.org/westurner/sphinxcontrib-rdf.png?branch=master
        :target: https://travis-ci.org/westurner/sphinxcontrib-rdf

.. .. image:: https://pypip.in/d/sphinxcontrib-rdf/badge.png
..        :target: https://crate.io/packages/sphinxcontrib-rdf?version=latest


Sphinx contrib extension for working with RDF and RDFLib

* Free software: BSD license

.. * Documentation: https://sphinxcontrib-rdf.rtfd.org/

Features
++++++++++
* See `TODO`_

TODO
++++++

Objectives

* reference objects with URIs (and [schema.org] types)
* output HTML with RDFa
  * Include RDFa blocks for existing Sphinx themes and templates
* include blocks of triples (like csv-table)


Syntax
-------
Line Blocks
~~~~~~~~~~~~~~
This works today, with no RDFa output ( https://github.com/westurner/tools/issues/2 ):

| Docs: https://wrdrd.com/docs/tools/#sphinx
| Src: https://github.com/westurner/tools/blob/master/index.rst

.. code:: rst

    .. index:: Sphinx
    .. _sphinx:
    
    Sphinx
    ~~~~~~~~~~~~~~~~~
    | Wikipedia: `<https://en.wikipedia.org/wiki/Sphinx_(documentation_generator)>`_
    | Homepage: https://pypi.python.org/pypi/Sphinx
    | Src: hg https://bitbucket.org/birkenfeld/sphinx/
    | Pypi: https://pypi.python.org/pypi/Sphinx
    | Docs: http://sphinx-doc.org/contents.html
    | Docs: http://sphinx-doc.org/markup/code.html
    | Docs: http://pygments.org/docs/lexers/
    | Docs: http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html
    | Docs: https://github.com/yoloseem/awesome-sphinxdoc
    
    
    Sphinx is a tool for working with
    :ref:`ReStructuredText` documentation trees
    and rendering them into HTML, PDF, LaTeX, ePub,
    and a number of other formats.

rdf directive
~~~~~~~~~~~~~~~
.. code:: restructuredtext

    I loved that |book|.
    
    .. |book| rdf:: awesome.com
       :a: schema:Book
       :title lang=en: Book Title
       :uri: awesome.com
       :author: sweet pete
       :oclc-isbn: 12345

questions:

* this is neither Turtle, nor JSON-LD, nor RDFa (which can be included as a literal HTML block); but docutils nearly supports this syntax without any external parsing libraries; so is *yet another format for [triples/JSONLD]* justifiable?

* how does this render the additional attributes as rdfa?

  * can it render (in HTML) as a tooltip?
    e.g. a docutils.nodes.span_with_tooltip?
    
    * tooltips do not work well with touch UIs and e.g. mobile devices.

* how does this compare to the sphinxcontrib bibtex approach[es]?
* what about PDF?

  * The PDF representation should look something like the output from a line block.

* how to reference multiple properties in-text with the same object
  definition?
  
  * https://github.com/python/core-workflow/issues/66#issuecomment-290797442
  
* See also:

  * https://github.com/noirbizarre/pelican-microdata/blob/master/microdata/plugin.py

Origins
--------
* http://westurner.github.io/self-directed-learning/slides.html#gap-sphinxcontrib-courses
* http://westurner.github.io/self-directed-learning/slides.html#gap-sphinx-glossary-thesarus
* http://lists.w3.org/Archives/Public/public-vocabs/2013Jul/0153.html
* http://docutils.sourceforge.net/docs/howto/rst-directives.html
* http://docutils.sourceforge.net/docs/ref/rst/directives.html#meta
* http://docutils.sourceforge.net/docs/ref/rst/directives.html#replacement-text
* http://docutils.sourceforge.net/docs/ref/rst/directives.html#unicode-character-codes
* http://sphinx-doc.org/ext/tutorial.html#the-directive-classes
* https://westurner.org/wiki/tools
* https://westurner.org/tools/
    
