.. ndic documentation master file, created by
   sphinx-quickstart on Fri Sep  2 16:23:42 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Ndic Documentation
******************

Ndic is Python package for NAVER English-Korean and Korean-English dictionaries.

Search of both English-Korean and Korean-English dictionaries is provided.

Ndic works by crawling the web http://endic.naver.com/. To crawl, it
uses `Requests`_ and `BeautifulSoup`_. Therefore, you should use it in **Internet Environments**.

Ndic supports Python Python 2.7 & 3.4–3.7 because `Requests officially
supports these versions.`_


Installation
============

Install via pip:

.. code-block:: bash

 pip install ndic

Quickstart
===========

The usage is very simple.

But, make sure that:

* Ndic is installed
* The user is connected to the Internet. 

Let's get started with some simple examples.

Search for Words
----------------

Begin by importing the Ndic module:

.. code-block:: python

    >>> import ndic

Entering an English word as the ``search`` function argument will return the
corresponding Korean word(s).

.. code-block:: python

    >>> ndic.search('apple')
    '사과'

Conversely, entering a Korean word as the ``search`` function argument will return
the corresponding English word(s).

.. code-block:: python

    >>> ndic.search('안녕하세요')
    'Hi!'

Multiple Definitions
--------------------

If the word you search has multiple meanings, you can choose the meaning of the desired order.

Unless you set any xth value, you will get the first meaning of the word.

.. code-block:: python

    >>> ndic.search('말', 1) # 1st meaning
    '(언어) word, language, speech, (literary) tongue'
    >>> ndic.search('말', 2) # 2nd meaning
    '(동물) horse'

Search for Phrases 
------------------

Phrases may also be searched.

.. code-block:: python

    >>> ndic.search('in order to')
    '(목적) 위하여'

Search for Nonexistent Words
----------------------------

Entering a nonexistent word as the ``search`` function argument will return the
empty string.

.. code-block:: python

    >>> ndic.search("aslkjfwe")
    ''
    >>> ndic.search("아댜리야")
    ''

Network Error
-------------

If your network connection is lost, you will get below error message.

.. code-block:: python

    >>> ndic.search('...')
    NdicConnectionError: Network connection is lost. Please check the connection to the Internet.

Command Line Interface
======================

Furthermore, Ndic supports CLI(Command Line System).

So you can use it
in command line and get the return value of the ``search`` fuction in terminals. It works
by `Click`_.

.. code-block:: bash

    $ ndic love
    (특히 가족・친구에 대한) 사랑
    $ ndic get --xth 2 # or -x 2
    얻다, 입수하다; 가지다(obtain)

.. _Requests: http://docs.python-requests.org/en/master/
.. _BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
.. _Requests officially supports these versions.: https://github.com/kennethreitz/requests#feature-support
.. _Click: http://click.pocoo.org/5/
