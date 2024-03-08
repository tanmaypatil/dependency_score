import gradio as gr

def add_numbers(x, y):
    return x + y

iface = gr.Interface(fn=add_numbers, inputs=["number", "number"], outputs="number")
iface.launch()
