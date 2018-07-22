from src.assesment_panda import Assesment_panda
import numpy as np 
import pandas as pd

def test_make_series():
    a = Assesment_panda()
    result = a.make_series(7, 4, ['a', 'b', 'c', 'd'])
    assert (isinstance(result, pd.Series))
    assert (result['a'], 7)
    assert (result['d'], 10)

    result = a.make_series(22, 5, ['a', 'b', 'c', 'd', 'hi'])
    assert (result['a'], 22)
    assert (result['d'], 25)
    assert (result['hi'], 26)


def test_data_frame_work():
    a = Assesment_panda()
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    colA, colB, colC = ('a', 'b', 'c')
    a.data_frame_work(df, colA, colB, colC)    
    assert df[colC].tolist() == [5, 7, 9]
    assert (colC in df.columns.tolist()) == True