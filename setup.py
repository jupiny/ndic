from setuptools import setup, find_packages


def get_requirements(filename):
    return open(filename).read().splitlines()

install_requires = get_requirements('requirements.txt')

setup(
  name='ndic',
  # packages = ['ndic'],
  packages=find_packages(),
  include_package_data=True,
  # py_modules=['ndic'],
  install_requires=install_requires,
  version='1.0',
  description='Python module for NAVER English-Korean and Korean-English dictionaries',
  author='jupiny',
  author_email='tmdghks584@gmail.com',
  url='https://github.com/jupiny/ndic',
  download_url='https://github.com/jupiny/ndic/tarball/1.0',
  # keywords = ['dictionary', 'translate', 'English', 'Korean', 'Naver'],
  classifiers=[],
  test_suite='nose.collector',
  tests_require=['nose'],
  entry_points='''
    [console_scripts]
    ndic=ndic.scripts.ndic:search
  ''',
)
