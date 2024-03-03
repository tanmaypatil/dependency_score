from score_params import * 
import pandas as pd


def calculate_score(row_params):
    score = 0
    err = None
    for column,value,weight in row_params:
      try:
        norm_value = params[column]["norm_function"](column,value) 
        weighted_value = norm_value * (weight /100)
        score += weighted_value
      except KeyError:
        score = 0
        err = f"key not found {column} norm_function"        
    return score ,err

def load_req():
    sheet_name='dependency'
    file_path='requirement.xlsx'
    # Read the worksheet into a pandas DataFrame
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df

def row_iterate_score(df):
    columns = params.keys()
    score_list = []
    for index, row in df.iterrows():
      row_params = []
      for column in columns:
        value = row [column]
        weight = params[column]["weight"]
        col_params = (column,value, weight)
        row_params.append(col_params)
      score =calculate_score(row_params)
      score_list.append(score) 
    df["score"] = score_list
    
    