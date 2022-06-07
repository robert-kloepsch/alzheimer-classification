import PySimpleGUI as sg

path_var = ""
#Draw the button
layout = [[sg.FileBrowse('Select Image', size=(30,4))],[sg.Button("Submit")]]
 
#Draw the window
window = sg.Window('GUI SAMPLE', layout, size=(200,150))


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Submit':
        path_var = list(values.values())[0]     
        break    