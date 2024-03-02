from score_params import * 
import pandas as pd


def calculate_score(row_params):
    score = 0
    for column,value,weight in row_params:
      norm_value = params[column]["function"](column,value) 
      weighted_value = norm_value * (weight /100)
      score += weighted_value
    return score 

def load_req():
    sheet_name='dependency'
    file_path='requirement.xlsx'
    # Read the worksheet into a pandas DataFrame
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df

def row_iterate():
    df = load_req()
    columns = params.keys()
    for index, row in df.iterrows():
      row_params = []
      for column in columns:
        value = row [column]
        weight = params[column]["weight"]
        col_params = (column,value, weight)
        row_params.append(col_params)
        calculate_score(row_params)  
    
    