from pylab import *
import unittest
from dfield import *

class DFieldTest(unittest.TestCase):


  def testSlopeSegment_slope1_at00(self):

    xs, ys = slopeSegment(0, 0, 1)
    
    self.assertEqual([round(-sqrt(2) / 4, 3), round(sqrt(2) / 4, 3)], [round(i, 3) for i in xs])
    self.assertEqual([round(-sqrt(2) / 4, 3), round(sqrt(2) / 4, 3)], [round(i, 3) for i in ys])
    
  def testSlopeSegment_slopeHalf_at00(self):
    
    xs, ys = slopeSegment(0, 0, 0.5)

    self.assertEqual([-4472.0, 4472.0], [round(i*(10**4)) for i in xs])    
    self.assertEqual([-2236.0, 2236.0], [round(i*(10**4)) for i in ys])
    
  def testSlopeSegment_slope2_at00(self):

    xs, ys = slopeSegment(0, 0, 2)

    self.assertEqual([-2236.0, 2236.0], [round(i*(10**4)) for i in xs])    
    self.assertEqual([-4472.0, 4472.0], [round(i*(10**4)) for i in ys])    
    


if __name__ == '__main__':
    unittest.main()

