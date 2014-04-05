import pyfav
version = pyfav.__version__

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

setup( 
    name = 'pyfav',
    version = version,
    url = 'http://github.com/phillipsm/pyfav',
    author = 'Matthew Phillips',
    author_email = 'matt@mattphillips.info',
    license = 'http://opensource.org/licenses/MIT',
    packages = find_packages(),
    install_requires = install_requires,
    description = 'You supply the URL, pyfav will supply the URL\'s favicon',
    long_description=open('README.md').read(),
    classifiers = filter(None, classifiers.split('\n')),
    test_suite = 'test',
)