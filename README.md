dfield is a small python application for plotting direction fields or [slope fields](http://en.wikipedia.org/wiki/Slope_field) in order to study first order differential equations.  Direction fields are useful for gaining an intuitive visual understanding of certain types of differential equations.  Usage requires installation of [matplotlib](http://matplotlib.sourceforge.net).

Usage
-----

Let's say you want to plot the differential equation

y' = x^2 + y^2 - 1

First we'll need to create a Python anonymous function:

`f = lambda x, y: x**2 + y**2 - 1`

then simply call:

```python
from dfield import *
draw(f)
```


Matplotlib will display a plot of the differential equation from (-2 < x < 2), (-2 < y < 2)

You can also provide the bounds for the plot yourself.  If you don't wish to use the -2:2 plot for the x, y axes, you may specify the bounds you'd like through arguments to `draw`.

For example:

```python
draw(f, minX=-8, maxX=0, minY=-1, maxY=4)
```