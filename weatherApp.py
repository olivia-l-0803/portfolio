import openmeteo_requests
import requests

import tkinter
from tkinter import *
#needed for the user interface

from temperature import curTemp, weekTemp
from getTime import curdate, curtime12, curtime24, weekday
#import from my own code!

Main = Tk("Weather App")
Main.config(bg="#F1DCA7")
Main.geometry("1000x600")
Main.resizable(False, False)
#Sets up the main window and also sets the size

Heading = Frame(master=Main, relief= "raised", bd=4, padx=10 ,pady=10)
Heading.config(bg= "#98BCD5")
Heading.place(relx= 0.01, rely= 0.01 , anchor= "nw" )
Headingcolor= Heading.cget("bg")

timeTitle = Label(master=Heading , padx= 10, pady = 10, font= ("Times New Roman", 35 ), bg= Headingcolor, text= curtime12)
timeTitle.pack()
dayTitle = Label(master=Heading, padx= 10, pady = 10, font= ("Times New Roman", 25 ) , bg= Headingcolor,  text= f"{weekday}, {curdate}")
dayTitle.pack()

currentTemp = Label(master=Heading, padx= 10, pady = 10, font= ("Times New Roman", 75 ) , bg= Headingcolor,  text= curTemp['Current Temperature'])
currentTemp.pack()
apparentTemp = Label(master=Heading, padx= 10, pady = 10, font= ("Times New Roman", 25 ) ,  bg= Headingcolor, text= f"Feels like: {curTemp['Apparent Temperature']}")
apparentTemp.pack()
# At a glance section



Label(master= Main , padx= 10, pady = 10, font= ("Times New Roman", 25 ), bg= Headingcolor, text= "Weekly Forecast").place(anchor="n", relx = 0.7, rely = 0.01)


Weekly = Frame(master=Main, relief= "raised", bd=4, padx=10 ,pady=10)
Weekly.config(bg= "lightblue1")
Weekly.place(relx= 0.6, rely= 0.2 , anchor= "n" )







Main.mainloop()