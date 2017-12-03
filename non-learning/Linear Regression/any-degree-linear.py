from numpy import mat, sum, array, arange, square
from numpy.linalg import solve
from matplotlib import pyplot as graph
from CustomMatT import diag_mat2
from pandas import read_csv

data = read_csv(r'../Database/demo.csv')

x = array(data['x'])
y = array(data['y'])

graph.scatter(x,y)

degree = int(input("Input Degree : "))

A = diag_mat2(degree + 1, func = lambda k : sum(x ** k))

B = mat([sum(x**i * y) for i in range(degree+1)]).T

p = solve(A , B)

predict = lambda x : sum((p[i] * (x ** (degree - i)) for i in range(degree + 1)))

L = arange(0,max(x) + 1, 0.1)

print("Cost : ", sum(square(y - predict(x))) / len(y))
print("Parameter : {}".format(p))

graph.plot(L,predict(L).T)

graph.show()
graph.close()
