from epics_process import * 
from pathlib import Path
import os

def test_fileexist():
    file_name = Path("requirements/requirement.xlsx")
    if file_name.exists():
        assert True
    else:
        print(f"{os.getcwd()}")
        assert False
        
def test_e2e():
    file_name = Path("requirements/requirement.xlsx")
    process_calc_draw(file_name,None)
    