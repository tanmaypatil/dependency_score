from score_params import * 
import pandas as pd

def scale_product_priority(priority):
    val = -4.9 * priority + 9.9 
    return val

def normalise(var_name ,x):
    limits = params[var_name]
    min = limits["min"]
    max = limits["max"]
    smin = scale["min"]
    smax = scale["max"]
    newValue = smin + ( x - min ) * ( smax - smin ) /( max - min)
    return newValue

def calculate_score(row):
    return None

def load_req():
    sheet_name='dependency'
    file_path='requirement.xlsx'
    # Read the worksheet into a pandas DataFrame
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df

def row_iterate():
  df = load_req()
  for index, row in df.iterrows():
    #print(index, row)
    print(f" dependency : {row['dependency']}")