import numpy as np
import pandas as pd


class Assessment:
    
    # PYTHON SECTION
    
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

    # Pandas SECTION

    def make_series(_self, start, length, index):
        return pd.Series(range(start, start + length), index)

    def data_frame_work(_self, df, colA, colB, colC):
        df[colC] = df[colA] + df[colB]