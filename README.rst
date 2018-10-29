Ndic
====

|Build Status| |Coverage Status| |Pypi Version| |Downloads| |License MIT|

Python package for NAVER English ⇔ Korean, Chinese ⇔ Korean dictionaries

Introduction
------------

Search of English ⇔ Korean, Chinese ⇔ Korean dictionaries is provided.

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

.. code-block:: bash

    $ pip install ndic

English Usage
-----

The usage is very simple.

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

If the word you search has multiple meanings, you can choose the meaning of the desired order.

Unless you set any ``xth`` value, you will get the first meaning of the word.

.. code-block:: python

    >>> ndic.search('말', 1) # 1st meaning
    '(언어) word, language, speech, (literary) tongue'
    >>> ndic.search('말', 2) # 2nd meaning
    '(동물) horse'

Phrases may also be searched.

.. code-block:: python

    >>> ndic.search('in order to')
    '(목적) 위하여'

Entering a nonexistent word as the ``search`` function argument will return the
empty string.

.. code-block:: python

    >>> ndic.search("aslkjfwe")
    ''
    >>> ndic.search("아댜리야")
    ''

If your network connection is lost, you will get below error message.

.. code-block:: python

    >>> ndic.search('...')
    NdicConnectionError: Network connection is lost. Please check the connection to the Internet.

Chinese Usage
-----

The usage is very similar with Chinese Usage.

Begin by importing the Ndic module:

.. code-block:: python

    >>> import ndic

Entering an English word as the ``search_zh`` function argument will return the
corresponding Korean word(s).

.. code-block:: python

    >>> ndic.search_zh('苹果')
    [
      {
         'origin': '苹果',
         'meanings': ['사과(나무).'],
         'pinyin': 'píngguǒ'
      }
    ]

Conversely, entering a Korean word as the ``search_zh`` function argument will return
the corresponding Chinese word(s).

.. code-block:: python

    >>> ndic.search_zh('사과')
    [
      {
         'origin': '사과',
         'meanings': ['苹果 。', '苹果树 (“사과나무”的略语)。'],
         'pinyin': ''
       }
    ]

If the word you search has multiple meanings, you can choose the meaning of the desired order.

Unless you set any ``num`` value, you will get the first meaning of the word.

.. code-block:: python

    >>> ndic.search_zh('抱歉', 1) # returns top 1 result
    [{'origin': '抱歉', 'meanings': ['미안하게 생각하다. 미안해하다.'], 'pinyin': 'bào//qiàn'}]
    >>> ndic.search_zh('抱歉', 4) # returns top 4 results
    [
      {'origin': '抱歉', 'meanings': ['미안하게 생각하다. 미안해하다.'], 'pinyin': 'bào//qiàn'},
      {'origin': '真抱歉', 'meanings': ['정말 미안해!'], 'pinyin': 'zhēnbàoqiàn'},
      {'origin': '抱歉的', 'meanings': ['regrettable'], 'pinyin': ''},
      {'origin': '感到抱歉', 'meanings': ['regretfully'], 'pinyin': ''}
    ]


English Command Line Interface
----------------------

Furthermore, Ndic supports CLI(Command Line System).

So you can use it
in command line and get the return value of the ``search`` fuction in terminals. It works
by `Click`_.

.. code-block:: bash

    $ ndic love
    (특히 가족・친구에 대한) 사랑
    $ ndic get --xth 2 # or -x 2
    얻다, 입수하다; 가지다(obtain)


Chinese Command Line Interface
----------------------

Furthermore, Ndic supports CLI(Command Line System).

So you can use it
in command line and get the returns stringied result of the ``search-zh`` fuction in terminals. It works
by `Click`_.

.. code-block:: bash

    $ ndic-zh 사랑
    사랑
    (异性之间的)爱 ，爱慕 ，爱意 ，爱河 ，爱情 ，感情 ，情 ，恋 ，恋爱 ，相思 ，...
    (父母、师长、神或上级的)爱 ，爱护 ，呵护 ，宠爱 ，关爱 ，慈 ，爱戴 。
    (对别人的)爱 ，爱心 ，爱护 ，关爱 ，友爱 。

    $ ndic-zh 노트북 --number 2 # or -n 2
    노트북
    笔记本电脑。

    노트북
    笔记本电脑，笔记本，手提电脑，便携式电脑，笔记型电脑，膝上电脑，膝上型计算机。

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
.. |Downloads| image:: https://pepy.tech/badge/ndic
   :target: https://pepy.tech/project/ndic
.. |License MIT| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/jupiny/ndic/master/LICENSE
