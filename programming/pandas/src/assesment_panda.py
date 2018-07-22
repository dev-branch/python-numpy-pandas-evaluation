import numpy as np 
import pandas as pd

class Assesment_panda:

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
        np_array = np.arange(start,start+length) 
        np_lst = np.array(index)           
        df = pd.Series(np_array,np_lst)
        return df    

    def data_frame_work(self,df, colA, colB, colC):
        '''
        INPUT: DATAFRAME, STR, STR, STR
        OUTPUT: None
        Insert a column (colC) into the dataframe that is the sum of colA and colB.
        Assume that df contains columns colA and colB and that these are numeric.
        '''
        df[colC] = df[colA]+df[colB]
       