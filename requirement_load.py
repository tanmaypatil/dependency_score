import pandas as pd 

def load_req():
  sheet_name='dependency'
  file_path='requirement.xlsx'
  # Read the worksheet into a pandas DataFrame
  df = pd.read_excel(file_path, sheet_name=sheet_name)
  print(df)
  


    