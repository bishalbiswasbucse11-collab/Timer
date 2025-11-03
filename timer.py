import time,os
from playsound3 import playsound
h,m,s=map(int,input("Enter hours,minutes and seconds: ").split())
timer=3600*h+60*m+s
for x in reversed(range (0,timer)):
    hours=int(x/3600)
    minutes=int(x/60)%60
    seconds=int(x%60)
    os.system('clear')
    print (f"Countdown : {hours:02} : {minutes:02} : {seconds:02}")
    time.sleep(1)
print ("Times up honey!!!")
playsound("bishal.mp3")