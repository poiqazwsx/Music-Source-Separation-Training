import gradio as gr
import os
DESCRIPTION = """
# audio sep
penis
"""

theme = gr.themes.Base(
    font=[gr.themes.GoogleFont('Libre Franklin'), gr.themes.GoogleFont('Public Sans'), 'system-ui', 'sans-serif'],
)
with gr.Blocks(css="footer{display:none !important}", theme=theme) as demo:
    gr.Markdown(DESCRIPTION)
    gr.DuplicateButton(
        value="Duplicate Space for private use",
        elem_id="duplicate-button",
        visible=os.getenv("SHOW_DUPLICATE_BUTTON") == "1",
    )
    gr.Markdown(value="hello")
    gr.Button(value="test")


demo.queue(max_size=20, api_open=False).launch(show_api=False)
