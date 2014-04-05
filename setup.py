import favicon
version = favicon.__version__

from setuptools import setup, find_packages

install_requires = [
    "beautifulsoup4>=4.3.2",
    "requests>=2.1.0",
]

classifiers = """
Intended Audience :: Developers
Intended Audience :: Science/Research
Natural Language :: English
License :: OSI Approved :: MIT License
Programming Language :: Python
Topic :: Internet :: WWW/HTTP
Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking
"""

import favicon

setup( 
    name = 'favicon',
    version = version,
    url = 'http://github.com/phillipsm/favicon',
    author = 'Matthew Phillips',
    author_email = 'matt@mattphillips.info',
    license = 'http://opensource.org/licenses/MIT',
    packages = find_packages(),
    install_requires = install_requires,
    description = 'Find and save a favicon given a URL',
    classifiers = filter(None, classifiers.split('\n')),
    test_suite = 'test',
)