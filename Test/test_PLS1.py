import numpy
import PLS.main
from scipy import sparse
import unittest

class CompletionTests(unittest.TestCase):
    """Tests checking whether the code doesn't crash while running PLS1."""
    
    @classmethod
    def setUpClass(self):
        self.xSmall = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
        self.ySmall = numpy.array([2,6,4])
    
    def test_pass_small(self):
        PLS.main.pls(self.xSmall, self.ySmall)


class CorrectnessTests(unittest.TestCase):
    """Tests checking the correctness of the output while running PLS1."""
    
    pass
    

if __name__ == '__main__':
    unittest.main()