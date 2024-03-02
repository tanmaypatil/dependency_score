from score import *

def test_score1():
    score_val = scale_product_priority(1.5)
    print(f"score is {score_val}")

def test_score2():
    score_val = scale_product_priority(1)
    #print(f"score is {score_val}")
    assert score_val == 5
    
def test_normal():
    n = normalise("requirement_effort",100)
    print(f"normalised score : {n}")
    assert n <= 5
    
def test_normal2():
    n = normalise("requirement_effort",200)
    print(f"normalised score : {n}")
    assert n <= 5

def test_iter_xls():
    row_iterate()
    
    
