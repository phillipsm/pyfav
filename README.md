##pyfav


pyfav is a Python library that helps you get a [favicon](http://en.wikipedia.org/wiki/Favicon) for a supplied URL.

Favicons can be annoying to track down because they're commonly located in a handful of different places. pyfav removes the annoyance by handling the details for you -- you supply a URL and pyfav will give you the favicon.

[![Build Status](https://travis-ci.org/phillipsm/pyfav.svg?branch=master)](https://travis-ci.org/phillipsm/pyfav)
[![Coverage Status](https://coveralls.io/repos/phillipsm/pyfav/badge.png?branch=master)](https://coveralls.io/r/phillipsm/pyfav?branch=master)

###Exchange a URL for a favicon on disk

The simplest way to get started is to use the download_favicon function,

````
from pyfav import download_favicon

favicon_saved_at = download_favicon('https://www.python.org/')
````

You should now see the favicon in your /tmp directory. If you want to control where the favicon gets written to disk,

````
from pyfav import download_favicon

mkdir /tmp/favicon-downloads

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

## License

Dual licensed under the MIT license (below) and [GPL license](http://www.gnu.org/licenses/gpl-3.0.html).

<small>
MIT License

Copyright (c) 2013 Matthew Phillips

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
</small>
