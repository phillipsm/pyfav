import unittest

from pyfav import retrieve

class PyFavTest(unittest.TestCase):
        
    def test_reteieve(self):
        retrieve('bing.com')
        self.assertEqual(1, 1)

def suite():
    test_suite = unittest.makeSuite(PyFavTest, 'test')
    return test_suite

if __name__ == '__main__':
    unittest.main()
    
    
    
# What to test:
# given markup, do we parse the <link tag as expected
# Do we save the favicon from from a url correctly? (test save function)
