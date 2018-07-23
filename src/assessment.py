import numpy as np
import pandas as pd


# PYTHON SECTION

def count_characters(string):
    '''
    INPUT: STRING
    OUTPUT: DICT (with counts of each character in input string)

    Return a dictionary which contains
    a count of the number of times each character appears in the string.
    Characters which with a count of 0 should not be included in the
    output dictionary.
    '''
    '''
    d = {}
    for char in string[::]:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d
    '''
    return {char: string.count(char) for char in string}

def invert_dictionary(d):
    '''
    INPUT: DICT
    OUTPUT: DICT (of sets of input keys indexing the same input values
                  indexed by the input values)

    Given a dictionary d, return a new dictionary with d's values
    as keys and the value for a given key being
    the set of d's keys which shared the same value.
    e.g. {'a': 2, 'b': 4, 'c': 2} => {2: {'a', 'c'}, 4: {'b'}}
    '''
    
    d_out = {}
    for char in d:
        if d[char] not in d_out:
            d_out[d[char]] = {char}
        else:
            d_out[d[char]].add(char)
    return d_out



def word_count(filename):
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
    nlin = 0
    nword = 0
    nchar = 0
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        nlin += 1
        nword += len(line.split(' '))
        nchar += len(line)

    return (nlin,nword,nchar)


def matrix_multiplication(A, B):
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
    '''
    result = [[0] * len(A[0])] * len(B)
    # iterate through rows of A
    for i in range(len(A)):
        # iterate through columns of B
        for j in range(len(B[0])):
            # iterate through rows of B
            for k in range(len(A[0])):
                result[i][j] += A[i][k] * B[k][j]
    return result
    '''
    '''
    M_dot = []
    for i in range(len(A)):
        new_row=[]
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(A[0])):
                sum += A[i][k]*B[k][j]
            new_row.append(sum)
        M_dot.append(new_row)
    return M_dot
    '''
    return [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

# NumPy SECTION

def array_work(rows, cols, scalar, matrixA):
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
    return np.dot(matrixA, np.full((rows, cols), scalar))


def boolean_indexing(arr, minimum):
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
    return arr[arr >= minimum]


# Pandas SECTION

def make_series(start, length, index):
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
    return pd.Series(range(start,start + length), index)


def data_frame_work(df, colA, colB, colC):
    '''
    INPUT: DATAFRAME, STR, STR, STR
    OUTPUT: None

    Insert a column (colC) into the dataframe that is the sum of colA and colB.
    Assume that df contains columns colA and colB and that these are numeric.
    '''
    df[colC] = df[colA] + df[colB]
    return df
