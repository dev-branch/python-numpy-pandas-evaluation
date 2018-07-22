import numpy as np
import pandas as pd

# PYTHON SECTION

class Assessment:
    def count_characters(_self, string):
        return {c: string.count(c) for c in string}

    def invert_dictionary(_self, d):
        result = {}
        for k,v in d.items():
            if v not in result:
                result[v] = {k}
            else:
                result[v].add(k)
        return result


    def word_count(_self, filename):
        with open('../data/alice.txt', 'r') as f:
            lines, words, chars = 0, 0, 0
            for line in f:
                lines += 1
                words += len(line.split())
                chars += len(line)
            return (lines, words, chars)

    def matrix_multiplication(_self, A, B):
        product = [[0]*len(B[0]) for x in range(len(A))]
        
        for A_row in range(len(A)):
            for B_column in range(len(B[0])):
                for B_row in range(len(B)):
                    product[A_row][B_column] += A[A_row][B_row] * B[B_row][B_column]
        return product

    # NumPy SECTION

    def array_work(_self, rows, cols, scalar, matrixA):
        return np.dot(matrixA, np.array([[scalar]*cols for row in range(rows)]))

    def boolean_indexing(_self, arr, minimum):
        return [arr[arr >= minimum]]

# # Pandas SECTION

# def make_series(start, length, index):
#     '''
#     INPUTS: INT, INT, LIST (of length "length")
#     OUTPUT: PANDAS SERIES (of "length" sequential integers
#              beginning with "start" and with index "index")
#
#     Create a pandas Series of length "length" with index "index"
#     and with elements that are sequential integers starting from "start".
#     You may assume the length of index will be "length".
#
#     E.g.,
#     In [1]: make_series(5, 3, ['a', 'b', 'c'])
#     Out[1]:
#     a    5
#     b    6
#     c    7
#     dtype: int64
#     '''
#     pass
#
#
# def data_frame_work(df, colA, colB, colC):
#     '''
#     INPUT: DATAFRAME, STR, STR, STR
#     OUTPUT: None
#
#     Insert a column (colC) into the dataframe that is the sum of colA and colB.
#     Assume that df contains columns colA and colB and that these are numeric.
#     '''
#     pass
