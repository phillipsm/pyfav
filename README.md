##pyfav


pyfav is a simple Python library that helps you find a [favicon](http://en.wikipedia.org/wiki/Favicon) for a supplied URL. Favicons can be annoying to track down because they're commonly located in a handful of place. pyfav saves you that annoyance by extracting away the details of finding the favicon location for you.


###Exchange a URL for a favicon on disk


The simplest way to get started is to use the download_favicon function.

To download a favicon for it's as simple as,

````
from favicon import download_favicon

download_favicon('https://www.python.org/')
````

If you want to be specific in where that favicon gets written to disk,

````
favicon_saved_at = download_favicon('https://www.python.org/', \
	file_prefix='python.org-', target_dir='/tmp/favicon-downloads')
````

###Get the location

If you'd prefer to handle the write to disk piece, use the get_favicon_url function by itself,
````
favicon_url = get_favicon_url('https://www.python.org/')
````


###Install

The easiest to get pyfav is through PIP

````
pip install pyfav
````

###License

pyfav is open source and freely avaiable under the [MIT License](http://opensource.org/licenses/MIT)