import pickle
from Python_Programs.holidays_marker import holidays_weekday_marker

def AQI_grade(AQI_Predicted): # Tells us about the grade of AQI given the AQI value

    # All the values are with respect to CPCB
    if 0<=AQI_Predicted<=50 :
        return "Good"
    elif 51<=int(AQI_Predicted)<=100:
        return "Satisfactory"
    elif 101<=int(AQI_Predicted)<=200:
        return "Moderate"
    elif 201<=int(AQI_Predicted)<=300:
        return "Poor"
    elif 301<=int(AQI_Predicted)<=400:
        return "Very Poor"
    elif 401<=int(AQI_Predicted)<=500:
        return "Severe"
    else:
        return "Severe"
# Made By Kunsh Bhatia
AQI_Color_Codes = ["#00E400","#FFFF00","#FF7E00","#FF0000","#8F3F97","#7E0023"]

def color_code_AQI(AQI_Predicted):
    if 0<=int(AQI_Predicted)<=50 :
        return AQI_Color_Codes[0]
    elif 51<=int(AQI_Predicted)<=100:
        return AQI_Color_Codes[1]
    elif 101<=int(AQI_Predicted)<=200:
        return AQI_Color_Codes[2]
    elif 201<=int(AQI_Predicted)<=300:
        return AQI_Color_Codes[3]
    elif 301<=int(AQI_Predicted)<=400:
        return AQI_Color_Codes[4]
    elif 401<=int(AQI_Predicted)<=500:
        return AQI_Color_Codes[5]
    else:
        return AQI_Color_Codes[5]

with open("Models/AQI_model.pkl","rb") as f:
    AQI_model = pickle.load(f)
# Made By Kunsh Bhatia
with open("Models/PM2,5_model.pkl","rb") as f:
    PM25_model = pickle.load(f)

with open("Models/PM10_model.pkl","rb") as f:
    PM10_model = pickle.load(f)

with open("Models/NO2_model.pkl","rb") as f:
    NO2_model = pickle.load(f)

with open("Models/SO2_model.pkl","rb") as f:
    SO2_model = pickle.load(f)

with open("Models/CO_model.pkl","rb") as f:
    CO_model = pickle.load(f)
    
with open("Models/Ozone_model.pkl","rb") as f:
    O3_model = pickle.load(f)

def main_function(Day,Month,Year):

    holiday,weekday_info = holidays_weekday_marker(Day,Month,Year)


    AQI_Predicted = AQI_model.predict([[Day,Month,Year,holiday,weekday_info]])[0]
    PM25_Predicted = PM25_model.predict([[Day,Month,Year,holiday,weekday_info]])[0]
    PM10_Prediction = PM10_model.predict([[Day,Month,Year,holiday,weekday_info]])[0]
    NO2_Prediction = NO2_model.predict([[Day,Month,Year,holiday,weekday_info]])[0]
    SO2_Prediction = SO2_model.predict([[Day,Month,Year,holiday,weekday_info]])[0]
    CO_Prediction = CO_model.predict([[Day,Month,Year,holiday,weekday_info]])[0]
    O3_Prediction = O3_model.predict([[Day,Month,Year,holiday,weekday_info]])[0]
    

    return (AQI_Predicted,PM25_Predicted,PM10_Prediction,NO2_Prediction,SO2_Prediction,CO_Prediction,
            O3_Prediction,AQI_grade(AQI_Predicted))

# To call :- AQI,PM25,PM10,NO2,SO2,CO,O3,Grade

Good = [
        "1) Enjoy outdoor activities freely 🌳",
        "2) Keep windows open for fresh air 🌬️",
        "3) Exercise outside as much as you like 🏃",
        "4) No need for masks or air purifiers 😌",
        "5) Maintain greenery around your home 🌏"
    ]
Satisfactory =  [
        "1) Sensitive groups should limit prolonged outdoor exertion 🚶‍♂️",
        "2) Ventilate indoor areas regularly ✨",
        "3) Avoid burning garbage or wood 🔥",
        "4) Stay hydrated and breathe easy 💧",
        "5) Monitor AQI updates if you're asthmatic 📱"
    ]
Moderate = [
        "1) People with asthma should avoid outdoor exercise 😷",
        "2) Use air purifiers indoors if possible 🌫️",
        "3) Avoid heavy traffic areas 🚗",
        "4) Keep kids and elderly indoors during peak hours 🧓👶",
        "5) Consider wearing N95 masks outside 😷"
    ]
Poor =  [
        "1) Limit outdoor activity to the minimum 🚷",
        "2) Avoid morning/evening walks near roads 🚶‍♀️❌",
        "3) Use air purifiers and keep windows shut 🌻",
        "4) Sensitive groups must stay indoors 🏠",
        "5) Consult doctor if breathing discomfort occurs 👨‍⚕️"
    ]
Very_Poor = [
        "1) Avoid all outdoor physical activities 🛑",
        "2) Keep children, elderly, and heart patients strictly indoors 👵👦",
        "3) Use N95 masks and air purifiers compulsorily 😷",
        "4) Refrain from using private vehicles unnecessarily 🚘❌",
        "5) Do not burn garbage or dry leaves 🔥🚫"
    ]
Severe = [
        "1) Everyone must stay indoors as much as possible 🏠⚠️",
        "2) Shut all windows and seal air leaks 🚪🔒",
        "3) Use room air filters and humidifiers 🌫️",
        "4) Avoid physical activities and exertion 💀",
        "5) Seek medical help if you feel breathless 🆘"
    ]


def Precautions(AQI_Predicted):
    if 0<=int(AQI_Predicted)<=50 :
        return Good
    elif 51<=int(AQI_Predicted)<=100:
        return Satisfactory
    elif 101<=int(AQI_Predicted)<=200:
        return Moderate
    elif 201<=int(AQI_Predicted)<=300:
        return Poor
    elif 301<=int(AQI_Predicted)<=400:
        return Very_Poor
    elif 401<=int(AQI_Predicted)<=500:
        return Severe
    else:
        return Severe


# Made By Kunsh Bhatia
