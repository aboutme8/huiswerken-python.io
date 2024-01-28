import unittest

class Testing(unittest.TestCase):
    def test_assertEqual(self):
        a = 'frikandel'
        b = 'frikandel'
        self.assertEqual(a, b)

    def test_assertTrue(self):
        a = True
        b = True
        self.assertTrue(a)
        self.assertTrue(b)

if __name__ == '__main__':
    unittest.main()
    
    
    
