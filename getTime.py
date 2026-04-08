import datetime
dt = datetime.datetime.now() #collects data
 
curdate = dt.strftime("%m/%d/%Y") #extracts date


curtime24 = dt.strftime("%H:%M") #extracts time!!

hour = int(curtime24[0:2]) #splitting into hour and minute!
min = curtime24[3:5]
if hour > 12: 
    hour -= 12
    curtime12 = f"{hour}:{min} PM"
else: 
    curtime12 = f"{hour}:{min} AM"

#weekday
num = datetime.datetime.today()
num = num.weekday()
#print(num)

abbreviation = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
weekday = abbreviation[num]


print(curdate, curtime24, curtime12, weekday) #<-testing
#get date and time!! 
