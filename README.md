# Ndic
[![Build Status](https://travis-ci.org/jupiny/ndic.svg?branch=master)](https://travis-ci.org/jupiny/ndic)

Python package for NAVER English-Korean and Korean-English dictionaries

## Introduction
Search of both English-Korean and Korean-English dictionaries is provided.

## Requirements
Ndic works by crawling the web <http://endic.naver.com/>. To crawl, it uses [Requests](http://docs.python-requests.org/en/master/) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

Therefore, you should use it in **Internet Environments**.

Ndic supports Python 2.6–2.7 & 3.3–3.5 because [Requests officially supports these versions.](https://github.com/kennethreitz/requests#feature-support)

## Installation
Install via pip:

```
$ pip install ndic
```

## Usage
The usage is very simple.

```
>>> import ndic
```
Entering an English word as the function argument will return the corresponding Korean word(s).

```
>>> ndic.search('apple')
'사과'
```
Conversely, entering a Korean word as the function argument will return the corresponding English word(s).

```
>>> ndic.search('안녕하세요')
'Hi!'
```
Phrases or words may also be searched.

```
>>> ndic.search('in order to')
'(목적) 위하여'
```

Entering a nonexistent word as the function argument will return the empty string.

```
>>> ndic.search("aslkjfwe")
''
>>> ndic.search("아댜리야")
''
```

If your network connection is lost, you will get below message.

```
>>> ndic.search('...')
'Network connection is lost. Please check the connection to the Internet.'
```

## Command Line Interface
Furthermore, Ndic supports CLI(Command Line System). So you can use it in command line and get the return value of Ndic in terminals. It works by [Click](http://click.pocoo.org/5/).

```
$ ndic love
(특히 가족・친구에 대한) 사랑
```
