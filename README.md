##pyfav


pyfav is a simple Python library that helps you get a [favicon](http://en.wikipedia.org/wiki/Favicon) for a supplied URL.

Favicons can be annoying to track down because they're commonly located in a handful of different places. pyfav removes the annoyance by handling the details for you -- you supply a URL and pyfav will give you the favicon.


###Exchange a URL for a favicon on disk

The simplest way to get started is to use the download_favicon function,

````
from pyfav import download_favicon

favicon_saved_at = download_favicon('https://www.python.org/')
````

You should now see the favicon in your /tmp directory. If you want to control where the favicon gets written to disk,

````
favicon_saved_at = download_favicon('https://www.python.org/', \
	file_prefix='python.org-', target_dir='/tmp/favicon-downloads')
````


###Get the location

If you'd prefer to handle the writing piece, use the get_favicon_url function,
````
from pyfav import get_favicon_url

favicon_url = get_favicon_url('https://www.python.org/')
````


###Install

The easiest to get pyfav is through PIP

````
pip install pyfav
````


###License

pyfav is open source and freely avaiable under the [MIT License](http://opensource.org/licenses/MIT)