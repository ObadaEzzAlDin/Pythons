
import PySimpleGUI as sg

import os.path
import gi


# First the window layout in 2 columns


file_list_column = [
        [sg.Text(text = "Sign language",auto_size_text=True)],

        [sg.Button('My Button',key='S',size = (50,5),focus=True)],
        [sg.Button('My Button2',key='Y',size = (50,5))],

]



layout = [

    [

        sg.Column(file_list_column),

       

    ]

]


window = sg.Window("Sign language", layout)



while True:

    event, values = window.read()
   

    if event == "Exit" or event == sg.WIN_CLOSED:

        break

    if event=='S':
        print("1")
        window.close()
        gi.first()
      

        

    if event=='Y':
        print("2")
    


window.close()