from src.assesment_py import Assesment_py
import numpy as np 

def test_count_characters():
    a = Assesment_py()
    string = "abafdcggfaabe"
    answer = {"a": 4, "b": 2, "c": 1, "d": 1, "e": 1, "f": 2, "g": 2}
    result = a.count_characters(string)
    assert result == answer

def test_invert_dictionary():
    a = Assesment_py()
    d = {"a": 4, "b": 2, "c": 1, "d": 1, "e": 1, "f": 2, "g": 2}
    result = {4: {'a'}, 2: {'b', 'f', 'g'}, 1: {'c', 'd', 'e'}}
    assert a.invert_dictionary(d) == result   