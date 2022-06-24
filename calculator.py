from ast import operator
from tkinter import CENTER
import PySimpleGUI as sg
from numpy import ravel_multi_index
operator=""
value=""
operand=""
#Define the win
#window's contents

layout = [
    [sg.Text(size=(20,1), key="display")],
    [sg.Button("1"),sg.Button("2"),sg.Button("3"),sg.Button("+")],
    [sg.Button("4"),sg.Button("5"),sg.Button("6"),sg.Button("-")],
    [sg.Button("7"),sg.Button("8"),sg.Button("9"),sg.Button("*")],
    [sg.Button("0"),sg.Button("/"),sg.Button("="),sg.Button("Quit")],
]
#create the window
window = sg.Window('CALCULATOR', layout)
#Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    #See if user wants to quit or window was closed
    
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    
    if event in [str(i) for i in range (10)]:
        value=value+event
        
        
        
    if event == "+" and operator=="":
        operand=int(value,10)
        value=""
        operator="+"
        
    if event == "=" and operator!="":
        operand2=int(value,10)
        if operator=="+":
            answer=operand+operand2
            value= f"{answer}"
            operand=""
            operator=""
            
            
    if event == "-" and operator=="":
        operand=int(value,10)
        value=""
        operator="-"
        
    if event == "=" and operator!="":
        operand2=int(value,10)
        if operator=="-":
            answer=operand-operand2
            value= f"{answer}"
            operand=""
            operator=""
        
        
    if event == "*" and operator=="":
        operand=int(value,10)
        value=""
        operator="*"
        
    if event == "=" and operator!="":
        operand2=int(value,10)
        if operator=="*":
            answer=operand*operand2
            value= f"{answer}"
            operand=""
            operator=""
            
            
    if event == "/" and operator=="":
        operand=int(value,10)
        value=""
        operator="/"
        
    if event == "=" and operator!="":
        operand2=int(value,10)
        if operator=="/":
            answer=operand/operand2
            value= f"{answer}"
            operand=""
            operator=""
            
            
            
    # if event == "" and operator=="":
    #     operand=int(value,10)
    #     value=""
    #     operator="+"
        
    # if event == "=" and operator!="":
    #     operand2=int(value,10)
    #     if operator=="+":
    #         answer=operand+operand2
    #         value= f"{answer}"
    #         operand=""
    #         operator=""
            
            
            
    #event.destroy()
    
    window['display'].update(f" operand operator value ")
#finish up by removing 
window.close()