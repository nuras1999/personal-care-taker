'''
CARETAKER  ~by  https://github.com/nuras1999
This tool wishes you thrice a day and remainds you about breakfast, lunch and dinner.
It even warns when you work more than 10pm or 11pm.
Additional feature -> it alerts when battery is low.
'''



import datetime as dt                                       #for current system time
from time import sleep                                      #for haulting program
from playsound import playsound                             #for playing audio files
from psutil import sensors_battery                          #for getting battery info

breakfastFlag = 0
lunchFlag = 0
dinnerFlag = 0
lateFlag = 0
tooLateFlag = 0
batteryLowFlag = 0

while(1):                                                   #for unlimited time
    
    currHour = dt.datetime.now().hour                       #current hour      
    currMinute = dt.datetime.now().minute                   #current minute

    #Battery Low Alert
    battery=sensors_battery()                               #getting battery details
    percent=(battery.percent)                               #getting battery details
    if percent <=20 and percent >=15 and batteryLowFlag == 0:       #if battery is less than 20%
        print("Battery low")
        playsound('audio\BatteryLow.mp3')
        batteryLowFlag=1

    #Alert at 10pm 
    if currHour == 22 and lateFlag == 0:
        print("It's getting late")
        playsound('audio\GettingLate.mp3')
        lateFlag=1

    #Alert at 11pm
    if currHour >= 23 and tooLateFlag == 0:
        print("It's too late")
        playsound('audio\TooLate.mp3')
        tooLateFlag=1

    #Wishing me 
    if currHour >= 1 and currHour <= 11:
        print("Hapie mrng Arun\n")
        playsound('audio\HappyMorning.mp3')
    elif currHour >= 12 and currHour <= 16:
        print("Hapie aftrnoon Arun\n")
        playsound('audio\HappyAfternoon.mp3')
    elif currHour >= 17 and currHour <= 21:
        print("Hapie evening Arun\n")
        playsound('audio\HappyEvening.mp3')

    #Food Remainder
    if (breakfastFlag==0 and currHour == 8):       
        print("Breakfast time. Go have your breakfast\n")
        playsound('audio\BreakfastTime.mp3')
        breakfastFlag=1
    elif (lunchFlag==0 and currHour == 13):         
        print("Lunch time. Go have your lunch\n")
        playsound('audio\LunchTime.mp3')
        lunchFlag=1
    elif (dinnerFlag==0 and currHour == 20):
        print("Dinner time. Go have your dinner\n")
        playsound('audio\DinnerTime.mp3')
        dinnerFlag=1
    
    sleep(60)                                             #Check time every 60 sec         