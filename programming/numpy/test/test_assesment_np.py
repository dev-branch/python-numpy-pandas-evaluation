from src.assesment_np import Assesment_np
import numpy as np 


def test_array_work():
    a = Assesment_np()
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
    assert (np.all(answer1 == result1))

    answer2 = np.array([[-36, -36],
                        [-18, -18],
                        [-30, -30],
                        [0, 0],
                        [-18, -18]])
    result2 = a.array_work(2, 2, 6, matrixA)
    assert (np.all(answer2 == result2))


def test_boolean_indexing():
    a = Assesment_np()
    arr = np.array([[-4, -4, -3],
                    [-1, 16, -4],
                    [-3, 6, 4]])

    result1 = a.boolean_indexing(arr, 0)
    answer1 = np.array([16, 6, 4])
    assert (np.all(result1 == answer1))

    result2 = a.boolean_indexing(arr, 10)
    answer2 = np.array([16])
    assert (np.all(result2 == answer2))