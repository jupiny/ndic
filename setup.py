from setuptools import setup


setup(
  name = 'ndic',
  packages = ['ndic'],
  # py_modules=['ndic'],
  install_requires = [
    'requests',
    'beautifulsoup4',
    'click',
  ],
  version = '0.5',
  description = 'Python module for NAVER English-Korean and Korean-English dictionaries',
  author = 'jupiny',
  author_email = 'tmdghks584@gmail.com',
  url = 'https://github.com/jupiny/ndic',
  download_url = 'https://github.com/jupiny/ndic/tarball/0.5',
  # keywords = ['dictionary', 'translate', 'English', 'Korean', 'Naver'],
  classifiers = [],
  entry_points='''
    [console_scripts]
    ndic=ndic.scripts.ndic:ndic
  ''',
)
