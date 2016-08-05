from setuptools import setup


setup(
  name = 'ndic',
  packages = ['ndic'],
  # py_modules=['ndic'],
  install_requires = [
    'requests',
    'beautifulsoup4',
    'click',
    'nose',
  ],
  version = '0.7',
  description = 'Python module for NAVER English-Korean and Korean-English dictionaries',
  author = 'jupiny',
  author_email = 'tmdghks584@gmail.com',
  url = 'https://github.com/jupiny/ndic',
  download_url = 'https://github.com/jupiny/ndic/tarball/0.7',
  # keywords = ['dictionary', 'translate', 'English', 'Korean', 'Naver'],
  classifiers = [],
  test_suite='nose.collector',
  tests_require=['nose'],
  entry_points='''
    [console_scripts]
    ndic=ndic.scripts.ndic:ndic
  ''',
)
