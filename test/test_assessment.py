import src.assessment as a
import numpy as np
import pandas as pd


def test_count_characters():
    string = "abafdcggfaabe"
    answer = {"a": 4, "b": 2, "c": 1, "d": 1, "e": 1, "f": 2, "g": 2}
    result = a.count_characters(string)
    assert result == answer


def test_invert_dictionary():
    d = {"a": 4, "b": 2, "c": 1, "d": 1, "e": 1, "f": 2, "g": 2}
    result = {4: {'a'}, 2: {'b', 'f', 'g'}, 1: {'c', 'd', 'e'}}
    assert result == a.invert_dictionary(d)


def test_word_count():
    #8449
    assert a.word_count('data/alice.txt') ==  (17, 1615, 8444)


def test_matrix_multiplication():
    A = [[2, 3, 4], [6, 4, 2], [-1, 2, 0]]
    B = [[8, -3, 1], [-7, 3, 2], [0, 3, 3]]
    answer = [[-5, 15, 20], [20, 0, 20], [-22, 9, 3]]
    assert np.array_equal(a.matrix_multiplication(A, B), answer)


def test_array_work():
    matrixA = np.array([[-4, -2],
                        [0, -3],
                        [-4, -1],
                        [-1, 1],
                        [-3, 0]])
    answer1 = np.array([[-24, -24, -24],
                        [-12, -12, -12],
                        [-20, -20, -20],
                        [0, 0, 0],
                        [-12, -12, -12]])
    result1 = a.array_work(2, 3, 4, matrixA)
    assert np.array_equal(answer1, result1)

    answer2 = np.array([[-36, -36],
                        [-18, -18],
                        [-30, -30],
                        [0, 0],
                        [-18, -18]])
    result2 = a.array_work(2, 2, 6, matrixA)
    assert np.array_equal(answer2, result2)


def test_make_series():
    result = a.make_series(7, 4, ['a', 'b', 'c', 'd'])
    assert (isinstance(result, pd.Series))
    assert result['a'] == 7
    assert result['d'] == 10

    result = a.make_series(22, 5, ['a', 'b', 'c', 'd', 'hi'])
    assert result['a'] == 22
    assert result['d'] == 25
    assert result['hi'] == 26


def test_data_frame_work():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    colA, colB, colC = ('a', 'b', 'c')
    a.data_frame_work(df, colA, colB, colC)
    assert colC in df.columns.tolist()
    assert df[colC].tolist() == [5, 7, 9]


def test_boolean_indexing():
    arr = np.array([[-4, -4, -3],
                    [-1, 16, -4],
                    [-3, 6, 4]])
    result1 = a.boolean_indexing(arr, 0)
    answer1 = np.array([16, 6, 4])
    assert np.array_equal(result1 , answer1)
    result2 = a.boolean_indexing(arr, 10)
    answer2 = np.array([16])
    assert (result2 , answer2)
