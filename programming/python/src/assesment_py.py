import numpy as np
class Assesment_py:
    
    def count_characters(self,str):
        
        '''
        INPUT: STRING
        OUTPUT: DICT (with counts of each character in input string)
        Return a dictionary which contains
        a count of the number of times each character appears in the string.
        Characters which with a count of 0 should not be included in the
        output dictionary.
        '''
        new_dic = {}
        for i in str:
            new_dic[i]=str.count(i)
        return new_dic    

    def invert_dictionary(self,d):
        '''
        INPUT: DICT
        OUTPUT: DICT (of sets of input keys indexing the same input values
                    indexed by the input values)
        Given a dictionary d, return a new dictionary with d's values
        as keys and the value for a given key being
        the set of d's keys which shared the same value.
        e.g. {'a': 2, 'b': 4, 'c': 2} => {2: {'a', 'c'}, 4: {'b'}}
        '''
        dic1={}
        for i in d.values():
            dic1[i]=i

        for k,v in dic1.items():
            dic1[k] = d.values(k)
        return dic1    