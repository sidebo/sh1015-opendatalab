from __future__ import print_function
import ipywidgets as widgets
from IPython.display import display
button = widgets.Button(description="Tip 1 fitting")
display(button)

def on_button_clicked(b):
    print("After calling histo.Fit(\"func\", \"S+\", ...) the fitted function can be accessed via histo.GetFunction(\"func\")" )

button.on_click(on_button_clicked)
