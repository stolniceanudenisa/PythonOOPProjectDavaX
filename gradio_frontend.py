import gradio as gr
import requests

API_URL = "http://localhost:8000/compute"  # or /compute_async

def call_api(operation, base=None, exponent=None, n=None):
    try:
        inputs = {}

        if operation == "power":
            inputs = {"base": base, "exponent": exponent}
        else:
            inputs = {"n": n}

        payload = {
            "operation": operation,
            "inputs": inputs
        }

        response = requests.post(API_URL, json=payload)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# UI Elements
def build_ui(operation):
    if operation == "power":
        return gr.update(visible=True), gr.update(visible=True), gr.update(visible=False)
    else:
        return gr.update(visible=False), gr.update(visible=False), gr.update(visible=True)

with gr.Blocks() as demo:
    gr.Markdown("# Math Microservice UI")

    operation = gr.Dropdown(choices=["power", "fibonacci", "factorial"], label="Select Operation")
    base = gr.Number(label="Base", visible=False)
    exponent = gr.Number(label="Exponent", visible=False)
    n = gr.Number(label="N", visible=False)

    operation.change(fn=build_ui, inputs=operation, outputs=[base, exponent, n])

    submit = gr.Button("Compute")
    output = gr.JSON(label="Result")

    submit.click(fn=call_api, inputs=[operation, base, exponent, n], outputs=output)

demo.launch()
