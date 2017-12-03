from numpy import mat, sum, array, arange
from numpy.linalg import solve
from matplotlib import pyplot as graph

x = array([1,2,3])
y = array([8,4,-10])

graph.scatter(x,y)

A = mat([
    [sum(x ** 2), sum(x),      len(x)],
    [sum(x ** 3), sum(x ** 2), sum(x)],
    [sum(x ** 4), sum(x ** 3), sum(x ** 2)]
])

B = mat([sum(y), sum(x * y), sum(x**2 * y)]).T

p = solve(A , B)

print(p)

predict = lambda x : p[0] * x**2 + p[1] * x + p[2]

L = arange(0,max(x) + 1, 0.1)

graph.plot(L ,predict(L).T)

graph.show()
graph.close()
