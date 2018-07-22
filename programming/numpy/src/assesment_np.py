
import numpy as np

class Assesment_np:   

    def array_work(self, rows, cols, scalar, matrixA):
        '''
        INPUT: INT, INT, INT, NUMPY ARRAY
        OUTPUT: NUMPY ARRAY
        (of matrix product of r-by-c matrix of "scalar"'s time matrixA)
        Create matrix of size (rows, cols) with elements initialized to the scalar
        value. Right multiply that matrix with the passed matrixA (i.e. AB, not
        BA).  Return the result of the multiplication.  You needn't check for
        matrix compatibililty, but you accomplish this in a single line.
        E.g., array_work(2, 3, 5, [[3, 4], [5, 6], [7, 8]])
           [[3, 4],      [[5, 5, 5],
            [5, 6],   *   [5, 5, 5]]
            [7, 8]]
        '''
        matrix1 = np.full((rows,cols),scalar)
        return np.dot(matrixA,matrix1)

    def boolean_indexing(self,arr, minimum):
        '''
        INPUT: NUMPY ARRAY, INT
        OUTPUT: NUMPY ARRAY
        (of just elements in "arr" greater or equal to "minimum")
        Return an array of only the elements of "arr" that are greater than or
        equal to "minimum"
        Ex:
        In [1]: boolean_indexing([[3, 4, 5], [6, 7, 8]], 7)
        Out[1]: array([7, 8])
        '''
        return arr[arr>minimum]
    pass    