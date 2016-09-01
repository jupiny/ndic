from setuptools import setup, find_packages
import os


ROOT = os.path.abspath(os.path.dirname(__file__))
VERSION = '1.1'

def get_requirements(filename):
    return open(os.path.join(ROOT, filename)).read().splitlines()

setup(
    name='ndic',
    packages=find_packages(),
    include_package_data=True,
    install_requires=get_requirements('requirements.txt'),
    tests_require=get_requirements('test-requirements.txt'),
    version=VERSION,
    description='Python module for NAVER English-Korean and Korean-English dictionaries',
    long_description=open(os.path.join(ROOT, 'README.md')).read(),
    author='jupiny',
    author_email='tmdghks584@gmail.com',
    url='https://github.com/jupiny/ndic',
    download_url='https://pypi.python.org/pypi/ndic',
    # keywords = ['dictionary', 'translate', 'English', 'Korean', 'Naver'],
    test_suite='nose.collector',
    entry_points='''
        [console_scripts]
        ndic=ndic.scripts.search:search
    ''',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Testing',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
