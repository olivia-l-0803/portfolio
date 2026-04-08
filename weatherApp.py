import openmeteo_requests
import requests

import tkinter
from tkinter import *
#needed for the user interface

from temperature import curTemp, weekTemp
from getTime import curdate, curtime12, curtime24, weekday
#import from my own code!

Main = Tk("Weather App")
Main.geometry("1000x600")
Main.resizable(False, False)
#Sets up the main window and also sets the size

Heading = Frame(master=Main, relief= "raised", bd=4, padx=10 ,pady=10)
Heading.config(bg= "lightblue1")
Heading.place(relx= 0.01, rely= 0.01 , anchor= "nw" )

timeTitle = Label(master=Heading , padx= 10, pady = 10, font= ("Times New Roman", 35 ) , text= curtime12)
timeTitle.grid(column=0, row= 0, columnspan= 2, sticky= "NSEW")
dayTitle = Label(master=Heading, padx= 10, pady = 10, font= ("Times New Roman", 25 ) , text= f"{weekday}, {curdate}")
dayTitle.grid(column=0, row= 1, columnspan= 2, sticky= "NSEW")

currentTemp = Label(master=Heading, padx= 10, pady = 10, font= ("Times New Roman", 75 ) , text= curTemp['Current Temperature'])
currentTemp.grid(column=0, row= 2, columnspan= 2, sticky= "NSEW")
apparentTemp = Label(master=Heading, padx= 10, pady = 10, font= ("Times New Roman", 25 ) , text= f"Feels like: {curTemp['Apparent Temperature']}")
apparentTemp.grid(column=0, row= 3, columnspan= 2, sticky= "NSEW")
# At a glance section

#Weekly = 




Main.mainloop()