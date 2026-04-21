""" 
def retrieveInformation():
     try: """

""" import requests

requests.get()
 """

#These are the coordinates of SITHS
#latitude 40.5679°
#longitude -74.1170°



x= "2019-07-04T18:00:00+00:00/PT3H"
year,day,month = x[0:4],x[5:7], x[8:10]

print(f"month: {month}, day: {day}, year: {year}")


#testing current date / time
import datetime
print(datetime.date.today())
print(datetime.datetime.now())


import customtkinter
from customtkinter import *


class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("tab 1")
        self.add("tab 2")

        # add widgets on tabs
        self.label = customtkinter.CTkLabel(master=self.tab("tab 1"))
        self.label.grid(row=0, column=0, padx=20, pady=10)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)


app = App()
app.mainloop()