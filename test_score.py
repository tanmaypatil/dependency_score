from score import *

def test_score1():
    score_val = scale_product_priority(1.5)
    print(f"score is {score_val}")

def test_score2():
    score_val = scale_product_priority(1)
    #print(f"score is {score_val}")
    assert score_val == 5
    
def test_normal():
    n = normalise("requirement effort",100)
    print(f"normalised score : {n}")
    assert n <= 5
    
def test_normal2():
    n = normalise("requirement effort",200)
    print(f"normalised score : {n}")
    assert n <= 5

def test_iter_xls():
    row_iterate()

def test_calc_score1():
    col1 = ("requirement effort",30,10)
    col2 = ("dependency effort",30,10)
    col3 = ("product priority",1.7,80)
    rows = []
    rows.append(col1)
    rows.append(col2)
    rows.append(col3)
    score = calculate_score(rows)
    print(f"score : {score}")

def test_calc_score2():
    col1 = ("requirement effort",30,10)
    col2 = ("dependency effort",30,10)
    col3 = ("product priority",1.1,80)
    rows = []
    rows.append(col1)
    rows.append(col2)
    rows.append(col3)
    score = calculate_score(rows)
    print(f"score : {score}")

def test_val_sprint():
    ans = sprint_val(None ,0)
    assert ans == False

def test_val_sprint1():
    ans = sprint_val(None ,3.5)
    assert ans == False

def test_val_sprint2():
    ans = sprint_val(None ,3)
    assert ans == True

def test_dict_neg():
    try :
      params["ABC"]
    except KeyError:
      print("key not found")

def test_calc_score3():
    """
    use 4 variables , requirement effort, dependency effort, product priority , arrival sprint 
    to calculate dependency score 
    """
    col1 = ("requirement effort",30,10)
    col2 = ("dependency effort",30,10)
    col3 = ("product priority",1.1,50)
    col4 = ("arrival sprint",4,30)
    rows = []
    rows.append(col1)
    rows.append(col2)
    rows.append(col3)
    rows.append(col4)
    score ,err = calculate_score(rows)
    assert err == None
    print(f"score : {score}")
   

    
