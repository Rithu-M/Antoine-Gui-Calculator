import PySimpleGUI as sg
from numpy.core.defchararray import isdigit

#-----------------------------------------------------------------------------------------------------------------------
# functions
def antoines(chem_name, T):
    import numpy as np
    import math

    names = ["methane", "ethylene", "propylene", "diethyl-ether", "ethanol", "isopropanol", "water"]

    coefficients = np.array(
        [[8.60416595e+00, 8.91226847e+02, -7.15000000e+00], [8.91667280e+00, 1.34039212e+03, -1.81500000e+01],
         [9.08255103e+00, 1.80090914e+03, -2.61500000e+01], [1.04238068e+01, 3.19719674e+03, 1.00000000e-02],
         [1.19040006e+01, 3.57228785e+03, -5.05000000e+01], [8.71597948e+00, 1.86550816e+03, -1.40190000e+02],
         [1.20483958e+01, 4.02356229e+03, -3.81500000e+01]])

    if chem_name.lower() in names:
        indexs = names.index(chem_name.lower())
        good_coeff = np.array((coefficients[indexs]))
        A = good_coeff[0]
        B = good_coeff[1]
        C = good_coeff[2]
        pvap = round(math.exp(A - B / (C + T)), 5)

    else:
        pvap="Notin"

    return pvap
#-----------------------------------------------------------------------------------------------------------------------

names = ["methane", "ethylene", "propylene", "diethyl-ether", "ethanol", "isopropanol", "water"]
# Define the window's contents
layout = [[sg.Text("Temperature")],
          [sg.Input(key='-T-')],
          [sg.Text("Chemical")],
          [sg.Combo(names, size=(10,10), key='-C-', enable_events=True)],
          [sg.Text(size=(60, 2), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window("Antoine's Equation", layout)

# Display and interact with the Window using an Event Loop

while True:
    event, values = window.read()
    Chemical = values['-C-']
    chem_name=Chemical.lower()
    T=values['-T-']
    if isdigit(T)==True:
        T = float(values['-T-'])
        pvap = antoines(Chemical, T)
    else:
        pvap="Notin"

    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window

    if pvap == "Notin":
        window['-OUTPUT-'].update('Please enter a valid temperature')
    else:
        window['-OUTPUT-'].update('The Vapor Pressure of ' + chem_name + " is " + str(pvap) + " bar")

# Finish up by removing from the screen
window.close()



