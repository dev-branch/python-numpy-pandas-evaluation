import numpy as np
import pandas as pd


# PYTHON SECTION

def count_characters(string):
    d = {}

    for char in string:
        if not (char in d):
            d[char] = 1
        else:
            d[char] = d[char] + 1

    return d



def invert_dictionary(d):
    d1= dict()  
    d2 = dict()  
    
    for key, val in d.items():
        if val in d1.keys():  
             d1[val].append(key)  
        else:
            d1[val]=list(key)  
   
    return d1  



def word_count(filename):
    with open('alice.txt', 'r') as f:
        lines, words, chars = 0, 0, 0 
        for line in f: 
            lines += 1
            words += len(line.split())
            chars += len(line)
        return (lines, words, chars) 


def matrix_multiplication(A, B):
   
    results = [[0]*len(B[0]) for x in range(len(A))]  
    for A_row in range(len(A)):  
        for B_column in range(len(B[0])):  
            for B_row in range(len(B)):
                results[A_row][B_column] += A[A_row][B_row] * B[B_row][B_column]  
    return results  


# NumPy SECTION


def array_work(rows, cols, scalar, matrixA):
    return(matrixA.dot(np.full((rows,cols),scalar))) 
  

def boolean_indexing(arr, minimum):
 
    return arr[arr >= minimum] 


# Pandas SECTION

def make_series(start, length, index):
    return pd.Series(range(start, start + length), index) 


def data_frame_work(df, colA, colB, colC):
    df[colC] = df[colA] + df[colB]   
    
    return df  

