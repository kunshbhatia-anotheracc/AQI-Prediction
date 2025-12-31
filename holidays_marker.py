# In this python file , we have a function which helps us getting the information such as ,the
# day provided is a holiday or not provided the date ( Day,Month and Year ) + it helps in getting which
# day of week is on the date ( Refer  "Information_About_Datasets.txt" for more info).
# Made By Kunsh Bhatia
import holidays
from datetime import date


def holidays_weekday_marker(Day,Month,Year):
    holidays_in = holidays.India()
    infomration_holiday = holidays_in.get(date(Year,Month,Day))


    if infomration_holiday == None:
        holiday = 0
    else:
        holiday = 1

    weekday_info = date(Year,Month,Day).weekday() + 1  # Weekday for today's date + is it sunday (holiday update)

    if weekday_info == 7 : 
        holiday = 1
    
    return holiday,weekday_info

# Made By Kunsh Bhatia