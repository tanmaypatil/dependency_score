import gradio as gr
from pathlib import Path
import os

def getlist():
    dir_name = Path("requirements")
    file_list=[]
    if dir_name.exists():
       file_list=os.listdir(dir_name) 
    else:
        print(f"{os.getcwd()}")
    return file_list

    

def showimg(file_name):
    print (f"file selected {file_name}")
    return 'result.svg'

demo = gr.Interface(
    fn=showimg,
    inputs =[gr.Dropdown(getlist(), label="requirement xlsx", info="select current PI requirement xlsx"),],
    outputs="image",
)
if __name__ == "__main__":
    demo.launch()

	