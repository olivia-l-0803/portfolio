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
    curtime12 = f"{hour}:{min} AM" #12 hr format

#weekday
num = datetime.datetime.today()
num = num.weekday()
#print(num)

abbreviation = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
weekday = abbreviation[num]


def findWeekday(daysahead: int):
    num = datetime.datetime.today()
    num = num.weekday()
    try:
        x = abbreviation[num + daysahead]
    except IndexError:

        x = abbreviation[daysahead- (7-num)]

    return x



print(curdate, curtime24, curtime12, weekday) #<-testing

print(findWeekday(1)) 
print(findWeekday(5)) 


#get date and time!! 