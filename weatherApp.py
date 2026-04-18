
import customtkinter as ctk
from customtkinter import *

#needed for the user interface

from getWeather import curTemp, weekTemp
from getTime import curdate, curtime12, curtime24, weekday
from getTime import findWeekday
#import from my own code!

Main = ctk.CTk(fg_color= ("#dfe8e6","#36365e")) #You can use tuples to store different colors! (Light, Dark)

Main.geometry("1000x600")
Main.resizable(False, False)

#setting up app window

ctk.set_appearance_mode("light")
Color1 = "#65737c"
Color2 = "#303e4b"
Font = "Poppins"
Fontcolor = "#CAD9E2"
#Theme Information  

Main.mainloop()
print("xx")