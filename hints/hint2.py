from __future__ import print_function
import ipywidgets as widgets
from IPython.display import display
button = widgets.Button(description="Give hint")
display(button)

def on_button_clicked(b):
    print("The bin content and uncertainty of a histogram can be accessed with `histo.GetBinContent(i)` and `histo.GetBinError(i)`" )

button.on_click(on_button_clicked)
