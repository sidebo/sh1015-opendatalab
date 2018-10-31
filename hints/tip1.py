from __future__ import print_function
import ipywidgets as widgets
from IPython.display import display
button = widgets.Button(description="Tip event loop")
display(button)

def on_button_clicked(b):
    print("[SWE] Ett snabbsätt att loopa över händelser i ett träd är att skriva 'for evt in tree: evt.branch...'")
    print("[ENG] A quick way to iterate over a tree is to write 'for evt in tree: evt.branch...'")

button.on_click(on_button_clicked)
