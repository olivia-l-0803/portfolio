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

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
 
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


app = App()
app.mainloop()
