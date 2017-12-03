from numpy import mat, sum, array, arange, square
from numpy.linalg import solve
from matplotlib import pyplot as graph
from logging import basicConfig, debug, DEBUG
from sys import stderr
from CustomMatT import diag_mat

#basicConfig(level=DEBUG)

x = array([1,2,3,4])
y = array([2,3,4,5])

graph.scatter(x,y)

degree = 2

A = mat([
    [sum(x ** 2), sum(x),      len(x)],
    [sum(x ** 3), sum(x ** 2), sum(x)],
    [sum(x ** 4), sum(x ** 3), sum(x ** 2)]
])

#A = diag_mat(degree + 1, func = lambda k : sum(x ** (k-1)))

B = mat([sum(x**i * y) for i in range(degree+1)]).T

p = solve(A , B)

debug("\nP : {}".format(p))

predict = lambda x : sum((p[i] * (x ** (degree - i)) for i in range(degree + 1)))

L = arange(0,max(x) + 1, 0.1)

print("Cost : ", sum(square(y - predict(x))))

graph.plot(L,predict(L).T)

graph.show()
graph.close()
