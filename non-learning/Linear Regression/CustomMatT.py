from typing import Callable
from numpy import diag, zeros

def diag_mat(deg : int, func : Callable[[int],int]  = lambda x : x) :
    A = diag([(func(deg)) / 2] * (deg), 0)

    for i in range(1, deg):
        A += diag([func(deg - i)] * (deg - i), i)

    A += A.T

    return A

def bounce_func(x,u) :
    return -abs(x - u) + u

def diag_mat2(deg : int, func : Callable[[int],int]  = lambda x : x) :

    A = zeros((deg, deg))

    for i in range(2 * deg - 1):
        T = diag([func(i)] * bounce_func(i + 1 , deg), deg - 1 - i)
        A += T

    #A += A.T

    return A

if __name__ == '__main__':
    pass

