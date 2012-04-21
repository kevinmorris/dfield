from pylab import *

SLOPE_SEGMENT_LENGTH = 0.1

def slopeSegment(x, y, df, slope_segement_length=1):
  
   xComponent = (cos(arctan(df)) * slope_segement_length) / 2
   yComponent = (sin(arctan(df)) * slope_segement_length) / 2

   return (x - xComponent, x + xComponent), (y - yComponent, y + yComponent)
