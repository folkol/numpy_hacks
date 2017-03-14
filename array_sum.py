import numpy as np
from time import perf_counter as pc
import matplotlib.pyplot as plt

N = 10000000

def list_comprehension(n):
    begin = pc()
    xs = [x for x in range(n)]
    s = sum(xs)
    end = pc() - begin
    print('Sum: %d' % s)
    return end

def generator_comprehension(n):
    begin = pc()
    xs = (x for x in range(n))
    s = sum(xs)
    end = pc() - begin
    print('Sum: %d' % s)
    return end

def np_array(n):
    begin = pc()
    ys = np.arange(0, n)
    s = ys.sum()
    end = pc() - begin
    print('Sum: %d' % s)
    return end

plt.plot([(generator_comprehension(n * N), list_comprehension(n * N), np_array(n * N)) for n in range(1, 8)])
#plt.plot([np_array(n * N) for n in range(10)])
plt.ylabel('Time (s)')
plt.xlabel('x %d' % N)
plt.legend(['Generator', 'List', 'narray'])
plt.title('Sum of range(0, N)')
plt.show()

