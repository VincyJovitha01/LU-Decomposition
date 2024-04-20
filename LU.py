# To print L and U matrix
import numpy as np
#add the library to import lu
from scipy.linalg import lu
A = np.array(eval(input()))
#add the code to get the L and U matrix
p,l,u=lu(a)
print(l)
print(u)



# To print X matrix (solution to the equations)
import numpy as np
#add the library to import lu_factor, lu_solve
from scipy.linalg import lu_factor,lu_solve
A = np.array(eval(input()))
b = np.array(eval(input()))
#add the code to get the solution of the matrix
lu,piv=lu_factor(a)
x=lu_solve((lu,piv),b)
print(x)

