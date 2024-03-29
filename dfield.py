from pylab import *

SLOPE_SEGMENT_LENGTH = 0.12
POINTS_PER_UNIT = 5

def draw(f, minX=-2, maxX=2, minY=-2, maxY=2):
  xp, yp = points(f, minX, maxX, minY, maxY)
  
  for i in range(len(xp)):
    plot(xp[i], yp[i], 'b')

def points(f, minX, maxX, minY, maxY):
  xp = []
  yp = []
  
  xs = arange(minX, maxX, 1 / float(POINTS_PER_UNIT))[1:]
  ys = arange(minY, maxY, 1 / float(POINTS_PER_UNIT))[1:]

  for x in xs:
    for y in ys:
      xc, yc = slopeSegment(x, y, f(x, y), SLOPE_SEGMENT_LENGTH)
      xp.append(xc)
      yp.append(yc)
      
  return xp, yp


def slopeSegment(x, y, df, slope_segement_length=1):
  
   xComponent = (cos(arctan(df)) * slope_segement_length) / 2
   yComponent = (sin(arctan(df)) * slope_segement_length) / 2

   return (x - xComponent, x + xComponent), (y - yComponent, y + yComponent)
