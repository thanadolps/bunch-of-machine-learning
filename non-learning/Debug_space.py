from numpy import array, diag, zeros
from typing import Callable
#from CustomMatT import diag_mat

K = array([1,2])

def bounce_func(x,u) :
    return -abs(x - u) + u

def diag_mat2(deg : int, func : Callable[[int],int]  = lambda x : x) :

    A = zeros((deg, deg))

    for i in range(2 * deg - 1):
        T = diag([i] * bounce_func(i + 1 , deg), i - 2)
        A += T

    #A += A.T

    return A

print(diag_mat2(3))
