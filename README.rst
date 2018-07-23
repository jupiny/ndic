Ndic
====

|Build Status| |Coverage Status| |Pypi Version| |Downloads Per Month| |License MIT|

Python package for NAVER English-Korean and Korean-English dictionaries

Introduction
------------

Search of both English-Korean and Korean-English dictionaries is
provided.

Requirements
------------

Ndic works by crawling the web http://endic.naver.com/. To crawl, it
uses `Requests`_ and `BeautifulSoup`_.

Therefore, you should use it in **Internet Environments**.

Ndic supports Python 2.7 & 3.4–3.7 because `Requests officially
supports these versions.`_

Installation
------------

Install via pip:

::

    $ pip install ndic

Usage
-----

The usage is very simple.

Begin by importing the Ndic module:

::

    >>> import ndic

Entering an English word as the ``search`` function argument will return the
corresponding Korean word(s).

::

    >>> ndic.search('apple')
    '사과'

Conversely, entering a Korean word as the ``search`` function argument will return
the corresponding English word(s).

::

    >>> ndic.search('안녕하세요')
    'Hi!'

Phrases may also be searched.

::

    >>> ndic.search('in order to')
    '(목적) 위하여'

Entering a nonexistent word as the ``search`` function argument will return the
empty string.

::

    >>> ndic.search("aslkjfwe")
    ''
    >>> ndic.search("아댜리야")
    ''

If your network connection is lost, you will get below error message.

::

    >>> ndic.search('...')
    NdicConnectionError: Network connection is lost. Please check the connection to the Internet.

Command Line Interface
----------------------

Furthermore, Ndic supports CLI(Command Line System).

So you can use it
in command line and get the return value of the ``search`` fuction in terminals. It works
by `Click`_.

::

    $ ndic love
    (특히 가족・친구에 대한) 사랑

.. _Requests: http://docs.python-requests.org/en/master/
.. _BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
.. _Requests officially supports these versions.: https://github.com/kennethreitz/requests#feature-support
.. _Click: http://click.pocoo.org/5/

.. |Build Status| image:: https://travis-ci.org/jupiny/ndic.svg?branch=master
   :target: https://travis-ci.org/jupiny/ndic
.. |Coverage Status| image:: https://coveralls.io/repos/github/jupiny/ndic/badge.svg?branch=master
   :target: https://coveralls.io/github/jupiny/ndic?branch=master
.. |Pypi Version| image:: https://img.shields.io/pypi/v/ndic.svg
   :target: https://pypi.python.org/pypi/ndic
.. |Downloads Per Month| image:: https://img.shields.io/pypi/dm/ndic.svg
   :target: https://pypi.python.org/pypi/ndic
.. |License MIT| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/jupiny/ndic/master/LICENSE
