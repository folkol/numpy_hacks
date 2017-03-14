import numpy as np
from sys import stdin

coords = np.loadtxt(stdin, dtype=np.int)

x, y = np.amin(coords, axis=0)
side = np.amax(coords - (x, y))

print(x, y, side)

