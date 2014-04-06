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

long_description = "pyfav is a simple Python library that helps you get a \
    favicon for a supplied URL. \
    Favicons can be annoying to track down because they're commonly located \
    in a handful of different places. pyfav removes the annoyance by handling \
    the details for you -- you supply a URL and pyfav will give you the \
    favicon."

setup( 
    name = 'pyfav',
    version = '0.1',
    url = 'http://github.com/phillipsm/pyfav',
    author = 'Matthew Phillips',
    author_email = 'matt@mattphillips.info',
    license = 'http://opensource.org/licenses/MIT',
    packages = find_packages(),
    install_requires = install_requires,
    description = 'You supply the URL, pyfav will supply the favicon',
    long_description=open('README.rst').read(),
    classifiers = filter(None, classifiers.split('\n')),
    keywords = ['favicon', 'favicons'],
    test_suite = 'test',
)