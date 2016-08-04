from setuptools import setup


setup(
  name = 'ndic',
  # packages = ['ndic'],
  py_modules=['ndic'],
  install_requires = [
    'requests',
    'beautifulsoup4',
  ],
  version = '0.2',
  description = 'NAVER Korean English dictionary',
  author = 'jupiny',
  author_email = 'tmdghks584@gmail.com',
  url = 'https://github.com/jupiny/ndic',
  download_url = 'https://github.com/jupiny/ndic/tarball/0.2',
  # keywords = ['dictionary', 'translate', 'English', 'Korean', 'Naver'],
  classifiers = [],
)
