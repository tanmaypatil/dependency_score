import gradio as gr

def showimg():
    return 'result.svg'

demo = gr.Interface(
    fn=showimg,
    inputs=None,
    outputs="image",
)
if __name__ == "__main__":
    demo.launch()

	