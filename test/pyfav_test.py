import unittest

from pyfav import parse_markup_for_favicon

class PyFavTest(unittest.TestCase):
        
    def test_parse_protocol_relative(self):
        """
        Sometimes a favicon is protocol relative (starts with //)
        """
        
        with open("test/relative-protocol.html") as f:
            markup = f.read()
        
        favicon_url = parse_markup_for_favicon(markup, 'https://stackoverflow.com/questions/4740473/setup-py-examples')
        self.assertEqual(favicon_url, 'https://cdn.sstatic.net/stackoverflow/img/favicon.ico?v=038622610830')


    def test_parse_relative_path(self):
        """
        Sometimes a favicon's path is relative (static/img/favicon.png)
        """
        
        with open("test/relative-path.html") as f:
            markup = f.read()
        
        favicon_url = parse_markup_for_favicon(markup, 'http://notesonthe.net')
        self.assertEqual(favicon_url, 'http://notesonthe.net/favicon.png')


    def test_parse_abs_path(self):
        """
        Sometimes a favicon's path is absolute (/static/img/favicon.png)
        """
        
        with open("test/abs-path.html") as f:
            markup = f.read()
        
        favicon_url = parse_markup_for_favicon(markup, 'http://bing.com')
        self.assertEqual(favicon_url, 'http://bing.com/s/a/bing_p.ico')
        
    def test_parse_no_favicon(self):
        """
        Sometimes there is no favicon in the markup
        """
        
        with open("test/no-favicon.html") as f:
            markup = f.read()
        
        favicon_url = parse_markup_for_favicon(markup, 'http://dolekemp96.org')
        self.assertEqual(favicon_url, None)


def suite():
    test_suite = unittest.makeSuite(PyFavTest, 'test')
    return test_suite

if __name__ == '__main__':
    unittest.main()