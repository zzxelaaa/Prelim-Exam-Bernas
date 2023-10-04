import unittest

def n():
    name = 'MIGUEL'

    return name

class myTest(unittest.TestCase):

    def test(self):

        self.assertEqual(n(),'MIGUEL')

if __name__ == '__main__':

    unittest.main()