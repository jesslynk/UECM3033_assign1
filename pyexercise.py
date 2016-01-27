import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.sqrt(x)*sy.exp(-x), (x,0, sy.oo))
    return ans
    
def my_solution():
    A = np.array( [[3,2,3,1,5,2,2,6,7,8], 
                   [1,2,4,4,6,4,9,3,6,8], 
                   [6,7,9,4,5,3,2,1,4,5],
                   [5,8,5,9,4,5,2,7,2,6],
                   [1,2,6,6,3,6,2,8,7,6],
                   [1,3,5,7,6,7,2,8,9,6],
                   [1,2,4,4,4,9,8,3,2,5],
                   [4,5,5,8,9,7,2,1,1,6],
                   [9,2,8,2,8,3,4,6,5,9],
                   [4,4,2,7,8,7,9,1,2,3],
                   ])
    b = np.array([9,8,3,5,1,7,8,9,2,6])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x    


if __name__ == '__main__':
    your_id = 1304565
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
