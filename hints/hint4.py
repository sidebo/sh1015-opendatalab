from __future__ import print_function
import ipywidgets as widgets
from IPython.display import display
button = widgets.Button(description="Tip get fit results")
display(button)

def on_button_clicked(b):
    print("[SWE] 'fitresult' är ett objekt av klassen 'TFitResult'. Ni kommer åt parametervärden med funktionsanropet 'Parameter(i)'. Titta på dokumentationen https://root.cern.ch/doc/master/classROOT_1_1Fit_1_1FitResult.html för att hitta funktionen som returnerar parameterosäkerhet." )
    print("[ENG] 'fitresult' is an object of class 'TFitResult'. The parameter values are obtained with function 'Parameter(i)'. Look at the documentation https://root.cern.ch/doc/master/classROOT_1_1Fit_1_1FitResult.html to find the function for retrieving parameter errors.")

button.on_click(on_button_clicked)
