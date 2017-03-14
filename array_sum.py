import numpy as np
from time import perf_counter as pc
import matplotlib.pyplot as plt

N = 10_000_000


def timed(f):
    def wrapped(*args):
        begin = pc()
        f(*args)
        end = pc() - begin
        return end

    return wrapped


@timed
def list_comprehension(n):
    return sum([x for x in range(n)])


@timed
def np_array(n):
    return np.arange(0, n).sum()


plt.plot([(list_comprehension(n * N), np_array(n * N)) for n in range(1, 10)])

plt.ylabel('Time (s)')
plt.xlabel('x %d' % N)
plt.legend(['Generator', 'List', 'narray'])
plt.title('Sum of range(0, N)')
plt.show()
