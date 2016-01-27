import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate(x**4 * sy.exp(-(x**2/2)), (x,0, sy.oo))
    return ans

def my_solution():
    A = np.array( [[3,1,4,5,-3,2,7,-10,1,2],
                   [1,2,-4,9,-1,1,3,2,-5,1],
                   [4,5,3,2,11,5,-6,1,3,-8],
                   [2,-3,3,4,1,-5,-4,8,1,2],
                   [-3,2,1,-1,6,8,5,5,1,3],
                   [1,-1,-7,12,2,3,6,-4,4,2],
                   [3,-4,-2,-3,5,13,2,7,1,1],
                   [7,12,8,6,-2,1,-3,3,1,4],
                   [-4,9,1,2,5,-1,2,3,6,1],
                   [8,6,3,1,-9,3,-2,4,-5,-2]
                   ] )
    b = np.array([23,-4,2,25,10,27,22,26,15,-11])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return np.around(x, decimals=3)


if __name__ == '__main__':
    your_id = 1203036
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
