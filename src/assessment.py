import numpy as np
import pandas as pd

class Assessment: 

    def __init__(self):
        pass
 
# PYTHON SECTION

    def count_characters(self,string):
        
        dict={}
        for i in string:
            if dict.get(i,'novalue')=='novalue':
                dict[i]=1
                      
            else:
                dict[i] +=1   
        return dict
        


    def invert_dictionary(self,d):
        
        dict_new={}
        s=set()
        for i,j in d.items():
            print(i,j)
            if dict_new.get(j,'novalue')=='novalue':
                dict_new[j]=set(i)
            else:
                s=dict_new.get(j)
                s.add(i)
                dict_new[j]=s
        
        return dict_new


        


    def word_count(self,filename):
        number_lines=0
        words=[]
        with open(filename,'r') as readfile:
            for line in readfile:
                number_lines+=1
                print(line)
                words+=line.split(" ")
                print(number_lines)
                char_count= [ len(i) for i in words]
                print("char_count",sum(char_count) )   
                print("words count",len(words))        
        return (number_lines, len(words), sum(char_count))
     

    def matrix_multiplication(self,X,Y):
        result=[[0,0,0],[0,0,0],[0,0,0]]
        for i in range(len(X)):
   # iterate through columns of Y
            for j in range(len(Y[0])):
                
       # iterate through rows of Y
                for k in range(len(Y)):
                    result[i][j] += X[i][k] * Y[k][j]
        return result            



# # NumPy SECTION


#def array_work(rows, cols, scalar, matrixA):


    def boolean_indexing(self,arr, minimum):
        return arr[arr>=minimum]



# # Pandas SECTION

    def make_series(self,start,length, index):
        list1=[]
        for i in range(start, start+length):
            list1.append(i)
        return pd.Series(list1,index)     

    def data_frame_work(self,df, colA, colB, colC):
        df[colC]=colA+colB
        return df
