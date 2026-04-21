

import customtkinter as ctk
from customtkinter import *
import PIL
from PIL import Image

#needed for the user interface

from getWeather import curTemp, weekTemp, interpretedCode, weekWeather, hourTemp, codeToPicture
from getTime import curdate, curtime12, curtime24, weekday, Hourlist
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
Color2 = ("#a0b3af","#36464e")
#Theme Information  

class Heading(ctk.CTkFrame): #Adds a large, easy to see section
    def __init__(self, master = Main):
        super().__init__(master = Main, fg_color= Color, corner_radius= 30, height= 175, width= 300)
        self.pack_propagate(False)
        self.place(relx= 0.2, rely= 0.2 , anchor= "center")

        self.currentTemp = ctk.CTkLabel(master=self, font= (Font, 75), anchor= "center",text_color= Fontcolor, fg_color="transparent", text= curTemp['Current Temperature']).pack(ipadx= 10, ipady= 10)
        self.apparentTemp = ctk.CTkLabel(master=self, font= (Font, 25 ) , anchor= "center", text_color= Fontcolor, fg_color="transparent", text= f"Feels like: {curTemp['Apparent Temperature']}").pack(ipadx= 10, ipady= 10)
        

class dateDisplay(ctk.CTkFrame): # creates a display for the date and time
    def __init__(self, master = Main):
        super().__init__(master = Main, fg_color= Color, corner_radius= 30,  height= 75, width= 175)
        self.pack_propagate(FALSE)
        self.place(relx= 0.5, rely= 0.1 , anchor= "center")


        self.timeTitle = ctk.CTkLabel(master=self , font= (Font, 20 ), anchor= "center", text_color= Fontcolor, fg_color="transparent", text= curtime12).pack(padx= 10, pady= (10,0))
        self.dayTitle = ctk.CTkLabel(master=self , font= (Font, 15 ), anchor= "center", text_color= Fontcolor, fg_color="transparent",  text= f"{weekday}, {curdate}").pack(padx= 10)
        

class addIcon(ctk.CTkLabel): # Image icon that shows current weather
    
    def __init__(self, master = Main, fileName = "icon/sunny.png"):
        super().__init__(master= Main, anchor= "center", fg_color= "transparent", text = "")
        
        pil_image = Image.open(fileName)
        pil_image.resize([100,100])
        self.ctkimage = ctk.CTkImage(light_image= pil_image, size= [100,100]) #stores image 
        self.configure(image = self.ctkimage)
        self.place(relx= 0.5, rely= 0.25 , anchor= "center")

        self.label = ctk.CTkLabel(master= Main, font= (Font, 15), anchor= "center", text_color= Fontcolor, fg_color="transparent",  text= interpretedCode[1]).place(relx= 0.5, rely= 0.35 , anchor= "center")


class WeeklyPanel(ctk.CTkFrame): #shows weekly highs and lows + an icon with weather
    def __init__(self):
        super().__init__(master = Main, fg_color= Color, corner_radius= 30,  height= 475, width= 325)
        self.grid_propagate(FALSE)
        self.place(relx= 0.8, rely= 0.55, anchor= "center")

        for i in range(0,7):
            ctk.CTkFrame(master = self, fg_color= Color, corner_radius= 30, border_width=3, border_color= Color2, height= 50, width= 300).pack(expand=True, fill=BOTH, in_= self, pady = 10, padx= 10)
            maxT = weekTemp[i][1]
            minT = weekTemp[i][2]
            date= weekTemp[i]
            DayofWeek = findWeekday(i+1)
            ctk.CTkLabel(master= self, font= (Font, 20), anchor= "center", text_color= Fontcolor, fg_color= "transparent", text= DayofWeek    ).grid(row= i, column=0, padx=(20, 10)) #adds the weekday
            ctk.CTkLabel(master= self, font= (Font, 17), anchor= "center", text_color= Fontcolor, fg_color="transparent", text= f"{maxT} (°F) | {minT} (°F)").grid(row= i, column=1,) #Max and Min temp
            

            pil_image = Image.open(weekWeather[i][0]).resize([100,100])
            ctkimage = ctk.CTkImage(light_image= pil_image, size= [40,40]) #stores image 
            ctk.CTkLabel(master= self, anchor= "center", fg_color="transparent", text= "", image= ctkimage).grid(row= i, column=2, padx= (20, 10))

            self.rowconfigure(index= i, weight= 1) #ensures all rows are equal


class HourlyTABS(ctk.CTkTabview): # a tab section with hourly updates
    def __init__(self, master= Main):
        super().__init__(master= Main, width= 575, height=350, corner_radius=30, fg_color= Color, segmented_button_fg_color= Color2, segmented_button_selected_color= Color , segmented_button_selected_hover_color= ("#e2f1ef","#879ba5"), segmented_button_unselected_color= Color2 ,segmented_button_unselected_hover_color=("#849b96","#26373f"), text_color= Fontcolor, text_color_disabled= Fontcolor)
        self.place(anchor = CENTER, relx = .325, rely=0.675 )
        self.grid_propagate(False)
         

        #adding each section!!
        self.add("Hourly Temps")
        self.add("Precipitation")



        # add widgets on hourly tab
        TemperaturePanel= ctk.CTkScrollableFrame(master= self.tab("Hourly Temps"), orientation="horizontal",  fg_color= Color,  height= 300, width= 550)
        TemperaturePanel.pack(expand= True, fill = BOTH)
        #TemperaturePanel.pack_propagate(False)

        for i in range(24):
            self.sections = ctk.CTkFrame(master = TemperaturePanel, fg_color= Color, corner_radius= 30, border_width=3, border_color= Color2, height= 270, width= 65)
            self.sections.pack(side= LEFT , expand=True, fill=BOTH, in_ = TemperaturePanel, pady = 5, padx= 10)
            self.sections.grid_propagate(False)


            HrT = hourTemp[0][i]
            HrAp = hourTemp[1][i]
            
            Hr = Hourlist[i]
            ctk.CTkLabel(master= self.sections, font= (Font, 15), anchor= "center", text_color= Fontcolor, fg_color= "transparent", text= Hr).grid(row= 0) #adds the hour
            ctk.CTkLabel(master= self.sections, font= (Font, 15), anchor= "center", text_color= Fontcolor, fg_color="transparent", text= f"{HrT}°F" ).grid(row= 2) #Temperature
            ctk.CTkLabel(master= self.sections, font= (Font, 15), anchor= "center", text_color= ("#687275","#A6BCC9"), fg_color="transparent", text= f"{HrAp}°F").grid(row= 3, pady = (0, 5)) #Apparent Temperature
            
            #adding little icon
            HrC = hourTemp[2][i]
            file= codeToPicture(HrC)
            pil_image = Image.open(file[0]).resize([100,100])
            ctkimage = ctk.CTkImage(light_image= pil_image, size= [40,40]) #stores image 
            ctk.CTkLabel(master= self.sections, anchor= "center", fg_color="transparent", text= "", image= ctkimage).grid(row= 1)
            
            for i in range(4): #everything! must be equal!
                self.sections.grid_rowconfigure(index=i,weight=1)
                self.sections.columnconfigure(index=0,weight=1)



x = Heading()
y= dateDisplay()
icon= addIcon(fileName= interpretedCode[0])
weekly = WeeklyPanel()
ctk.CTkLabel(master= Main, font= (Font, 30 ), anchor= "center", text_color= Fontcolor, fg_color="transparent", text= "Weekly Forecast").place(relx= 0.8, rely= 0.075, anchor= "center")# a label for the weekly section
Hour= HourlyTABS(Main)

Main.mainloop()
print("xx App closed")