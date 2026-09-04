import unittest
from cliforge import parse_flags
class Tests(unittest.TestCase):
 def test_parse(self): self.assertEqual(parse_flags(['--name','medu','--verbose']),{'name':'medu','verbose':True})
if __name__=='__main__': unittest.main()
