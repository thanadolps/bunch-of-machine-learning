from numpy import mat, sum, array, arange, square
from numpy.linalg import solve
from matplotlib import pyplot as graph
from CustomMatT import diag_mat2

x = array([1,2,3,4])
y = array([1,4,9,16])

graph.scatter(x,y)

degree = int(input("Input Degree : "))

A = diag_mat2(degree + 1, func = lambda k : sum(x ** k))

B = mat([sum(x**i * y) for i in range(degree+1)]).T

p = solve(A , B)

predict = lambda x : sum((p[i] * (x ** (degree - i)) for i in range(degree + 1)))

L = arange(0,max(x) + 1, 0.1)

print("Cost : ", sum(square(y - predict(x))))

graph.plot(L,predict(L).T)

graph.show()
graph.close()
