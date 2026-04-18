#laying a foundation with TKinter. This is not the final product


import tkinter
from tkinter import *
#needed for the user interface

from getWeather import curTemp, weekTemp
from getTime import curdate, curtime12, curtime24, weekday
from getTime import findWeekday
#import from my own code!

Main = Tk("Demo")
Color1 = "#65737c"
Color2 = "#303e4b"
Font = "Poppins"
Fontcolor = "#CAD9E2"
#Theme Information


Main.config(bg=Color1)
Main.geometry("1000x600")
Main.resizable(False, False)
#Sets up the main window and also sets the size

Heading = Frame(master=Main, bd=4, padx=10 ,pady=10)
Heading.config(bg= Color2)
Heading.place(relx= 0.01, rely= 0.01 , anchor= "nw" )


timeTitle = Label(master=Heading , padx= 10, pady = 10, font= (Font, 35 ), bg= Color2, fg= Fontcolor, text= curtime12)
timeTitle.pack()
dayTitle = Label(master=Heading, padx= 10, pady = 10, font= (Font, 25 ) , bg= Color2, fg= Fontcolor, text= f"{weekday}, {curdate}")
dayTitle.pack()

currentTemp = Label(master=Heading, padx= 10, pady = 10, font= (Font, 75 ) , bg= Color2, fg= Fontcolor, text= curTemp['Current Temperature'])
currentTemp.pack()
apparentTemp = Label(master=Heading, padx= 10, pady = 10, font= (Font, 25 ) ,  bg= Color2, fg= Fontcolor, text= f"Feels like: {curTemp['Apparent Temperature']}")
apparentTemp.pack()
# 'At a glance' section


Label(master= Main , padx= 10, pady = 10, font= (Font, 30 ), bg= Color2, fg= Fontcolor, text= "Weekly Forecast").place(anchor="n", relx = 0.68, rely = 0.01)


Weekly = Frame(master=Main, bd=4, padx=5 ,pady=10)
Weekly.config(bg= Color2)
Weekly.place(relx= 0.68, rely= 0.2 , anchor= "n" )

for i in range(0,7):
    maxT = weekTemp[i][1]
    minT = weekTemp[i][2]
    date= weekTemp[i]
    DayofWeek = findWeekday(i+1)
    Label(master= Weekly, font= (Font, 20), bg= Color2, fg= Fontcolor, text= DayofWeek).grid(row= 0, column=i, padx= 5)
    Label(master= Weekly, font= (Font, 20), bg= Color2, fg= Fontcolor, text= maxT).grid(row= 1, column=i, padx= 10)
    Label(master= Weekly, font= (Font, 20), bg= Color2, fg= Fontcolor, text= minT).grid(row= 2, column=i, padx= 10)
    



Main.mainloop()