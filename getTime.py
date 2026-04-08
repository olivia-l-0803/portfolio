import datetime
dt = str(datetime.datetime.now()) #collects data
curdate = dt[0:10] #extracts date
curtime24 = dt[11:16] #extracts time!!

hour = int(curtime24[0:2]) #splitting into hour and minute!
min = int(curtime24[3:5])  
if hour > 12: 
    hour -= 12
    curtime12 = f"{hour}:{min} PM"
else: 
    curtime12 = f"{hour}:{min} AM"



print(curdate, curtime24, curtime12)
#get date and time