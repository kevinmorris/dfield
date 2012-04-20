from pylab import *
import unittest
from dfield import *

class DFieldTest(unittest.TestCase):


  def testSlopeSegment_slope1_at00(self):

    xs, ys = slopeSegment(0, 0, 1)
    
    self.assertEqual([round(-sqrt(2) / 4, 3), round(sqrt(2) / 4, 3)], [round(i, 3) for i in xs])
    self.assertEqual([round(-sqrt(2) / 4, 3), round(sqrt(2) / 4, 3)], [round(i, 3) for i in ys])
    


if __name__ == '__main__':
    unittest.main()

