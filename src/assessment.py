import numpy as np
import pandas as pd


# PYTHON SECTION
class Assessment: 
    
    def __init__(self):
        pass
    
    def count_characters(self, string):
    '''
    INPUT: STRING
    OUTPUT: DICT (with counts of each character in input string)

    Return a dictionary which contains
    a count of the number of times each character appears in the string.
    Characters which with a count of 0 should not be included in the
    output dictionary.
    '''
        letters = []
        for i in range(len(string)):
            letters.append(string[i])
        dict_letters = {letter: letters.count(letter) for letter in letters}
        return dict_letter
    
    def invert_dictionary(self, d):
    '''
    INPUT: DICT
    OUTPUT: DICT (of sets of input keys indexing the same input values
                  indexed by the input values)

    Given a dictionary d, return a new dictionary with d's values
    as keys and the value for a given key being
    the set of d's keys which shared the same value.
    e.g. {'a': 2, 'b': 4, 'c': 2} => {2: {'a', 'c'}, 4: {'b'}}
    '''
        letters = []
        counts = []
        for letter in d:
            letters.append(letter)
        for letter in d:
            counts.append(d[letter])
        inv_dict = {}
        for count in counts:
            if count not in inv_dict:
                inv_dict.update({count : []})
        for letter in d:
            if d[letter] in inv_dict:
                inv_dict[d[letter]].append(letter)
        return inv_dict


    def word_count(self, filename):
    '''
    INPUT: STRING
    OUTPUT: INT, INT, INT (a tuple with line, word,
                           and character count of named INPUT file)

    The INPUT filename is the name of a text file.
    The OUTPUT is a tuple containting (in order)
    the following stats for the text file:
      1. number of lines
      2. number of words (broken by whitespace)
      3. number of characters
    '''
        num_char = len(filename)
        lines = 0
        for line in open(filename):
            lines += 1
        num_words = len(filename.split())
        return num_char, num_words, lines    


    def matrix_multiplication(self, A, B):
    '''
    INPUT: LIST (of length n) OF LIST (of length n) OF INTEGERS,
            LIST (of length n) OF LIST (of length n) OF INTEGERS
    OUTPUT: LIST OF LIST OF INTEGERS
            (storing the product of a matrix multiplication operation)

    Return the matrix which is the product of matrix A and matrix B
    where A and B will be (a) integer valued (b) square matrices
    (c) of size n-by-n (d) encoded as lists of lists.

    For example:
    A = [[2, 3, 4], [6, 4, 2], [-1, 2, 0]] corresponds to the matrix

        | 2  3  4 |
        | 6  4  2 |
        |-1  2  0 |

    Please do not use numpy. Write your solution in straight python.
    '''
        c = []
        for i in range(0,len(A)):
            temp=[]
            for j in range(0,len(B[0])):
                s = 0
                for k in range(0,len(A[0])):
                    s += A[i][k]*B[k][j]
                temp.append(s)
            c.append(temp)
        return c



# NumPy SECTION


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
        arrayA = np.array(matrixA)
        multiplied = arrayA * scalar
        return multiplied.reshape(rows, cols)


    def boolean_indexing(self, arr, minimum):
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
        atleast = []
        for row in arr:
            for num in row:
                if num >= minimum:
                    atleast.append(num)
        return np.array(atleast)


# Pandas SECTION

    def make_series(self, start, length, index):
    '''
    INPUTS: INT, INT, LIST (of length "length")
    OUTPUT: PANDAS SERIES (of "length" sequential integers
             beginning with "start" and with index "index")

    Create a pandas Series of length "length" with index "index"
    and with elements that are sequential integers starting from "start".
    You may assume the length of index will be "length".

    E.g.,
    In [1]: make_series(5, 3, ['a', 'b', 'c'])
    Out[1]:
    a    5
    b    6
    c    7
    dtype: int64
    '''
        data = []
        for i in range(len(index)):
            data.append(start + i)
        return pd.Series(data = data, index = index)   

    def data_frame_work(self,df, colA, colB, colC):
        df[colC]=colA+colB
        return df

