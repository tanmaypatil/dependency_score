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

def test_round_val():
    assert( round(10.152,2)== 10.15)

def test_score_df_1row():
    df = pd.DataFrame( {'requirement effort' : [30] ,'dependency effort' : [30],
                        'product priority' :[1.1],'arrival sprint' : [4]  } )
    row_iterate_score(df)
    assert(df.loc[0,"score"] != 0)
    print(df.loc[0,"score"])
    
def test_score_df_2row():
    df = pd.DataFrame( {'requirement effort' : [30,60,60,60] ,'dependency effort' : [30,30,60,60],
                        'product priority' :[1.1,1.1,1.1,1.0],'arrival sprint' : [4,4,4,4]  } )
    row_iterate_score(df)
    # check for score at index location 0
    assert(df.loc[0,"score"] != 0)
    print(df.loc[0,"score"])
    # check for score at index location 1
    assert(df.loc[1,"score"] != 0)
    print(df.loc[1,"score"])
    # check for score at index location 2
    assert(df.loc[2,"score"] != 0)
    print(df.loc[2,"score"])
    # check for score at index location 3
    assert(df.loc[3,"score"] != 0)
    print(df.loc[3,"score"])

def test_remove_frset():
    s = set()
    s.add(1)
    try:
      s.remove(5)
    except KeyError:
      print("key 5 not found")  
    
    

    
   

    
