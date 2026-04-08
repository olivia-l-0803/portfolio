import openmeteo_requests
import requests
import tkinter
from tkinter import *
#needed for the user interface

from temperature import getCurrentTemp, getTempWeek
#import from my own code!

import datetime
dt = str(datetime.datetime.now())
curdate = dt[0:10]
curtime = dt[11:16]
print(curdate, curtime)
#get date and time

Main = Tk("Weather App")
Main.geometry("1000x600")
Main.resizable(False, False)
#Sets up the main window and also sets the size

Heading = Frame(master=Main, padx= 10, pady= 10, relief="raised", height= 400, width= 400)
Heading.place(anchor= NW)





Main.mainloop()