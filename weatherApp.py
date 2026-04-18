
from typing import Any, Tuple

import customtkinter as ctk
from customtkinter import *
import PIL
from PIL import Image

#needed for the user interface

from getWeather import curTemp, weekTemp
from getTime import curdate, curtime12, curtime24, weekday
from getTime import findWeekday
#import from my own code!

Main = ctk.CTk(fg_color= ("#dfe8e6","#819daa")) #You can use tuples to store different colors! (Light, Dark)

Main.geometry("1000x600")
Main.resizable(False, False)

#setting up app window

ctk.set_appearance_mode("light")
Font = "Inter"
Fontcolor = ("#4a5356","#CAD9E2")
Color = ("#c4d6d3","#627c89")
#Theme Information  

class Heading(ctk.CTkFrame):
    def __init__(self, master = Main):
        super().__init__(master = Main, fg_color= Color, corner_radius= 30, height= 175, width= 300)
        self.pack_propagate(False)
        self.place(relx= 0.2, rely= 0.2 , anchor= "center")

        self.currentTemp = ctk.CTkLabel(master=self, font= (Font, 75), anchor= "center",text_color= Fontcolor, fg_color="transparent", text= curTemp['Current Temperature']).pack(ipadx= 10, ipady= 10)
        self.apparentTemp = ctk.CTkLabel(master=self, font= (Font, 25 ) , anchor= "center", text_color= Fontcolor, fg_color="transparent", text= f"Feels like: {curTemp['Apparent Temperature']}").pack(ipadx= 10, ipady= 10)
        

class dateDisplay(ctk.CTkFrame):
    def __init__(self, master = Main):
        super().__init__(master = Main, fg_color= Color, corner_radius= 30,  height= 75, width= 175)
        self.pack_propagate(FALSE)
        self.place(relx= 0.45, rely= 0.1 , anchor= "center")


        self.timeTitle = ctk.CTkLabel(master=self , font= (Font, 20 ), anchor= "center", text_color= Fontcolor, fg_color="transparent", text= curtime12).pack(padx= 10, pady= (10,0))
        self.dayTitle = ctk.CTkLabel(master=self , font= (Font, 15 ), anchor= "center", text_color= Fontcolor, fg_color="transparent",  text= f"{weekday}, {curdate}").pack(padx= 10)
        
        
class addIcon(ctk.CTkLabel):
    
    def __init__(self, master = Main, fileName = "22.png"):
        super().__init__(master= Main, anchor= "center", fg_color= "transparent", text = "")
        
        pil_image = Image.open(fileName)
        pil_image.resize([100,100])
        self.ctkimage = ctk.CTkImage(light_image= pil_image, size= [100,100]) #stores image 
        self.configure(image = self.ctkimage)
        self.place(relx= 0.45, rely= 0.25 , anchor= "center")
        
x = Heading()
y= dateDisplay()
icon= addIcon()

Main.mainloop()
print("xx")