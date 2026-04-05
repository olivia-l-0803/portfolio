import openmeteo_requests
import requests
import tkinter
from tkinter import *
#needed for the user interface

from temperature import getCurrentTemp, getTempWeek
#import from my own code!

Main = Tk("Weather App")
Main.geometry("1000x600")
Main.resizable(False, False)
#Sets up the main window and also sets the size

Heading = Frame(master=Main, background= "Powder Blue")



Main.mainloop()