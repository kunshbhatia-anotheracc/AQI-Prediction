import pandas as pd
from Python_Programs.backend_processing import main_function
# Made By Kunsh Bhatia
def AQI_Using_Params(Date,Month,Year):
    AQI,PM25,PM10,NO2,SO2,CO,O3,Grade = main_function(Date,Month,Year)
    rq_list = ['PM25','PM10','NO2','SO2','CO','O3']
    rq_values = [PM25,PM10,NO2,SO2,CO,O3]
    Color_Codes = ["#00E400","#FFFF00","#FF7E00","#FF0000","#8F3F97","#7E0023"]

    AQI_Pred_using_Params = []
    color_codes_params = []
    for i in range(len(rq_list)):
        df = pd.read_csv(f"AQI_Cal/AQI_{rq_list[i]}.xlsx")

        for k in df['Low']:
            if k<=rq_values[i]:
                rq = df[df['Low'] == k]

        Conc_Low = rq['Low'].values[0]
        Conc_High = rq['High'].values[0]
        AQI_Low = rq['AQI_Low'].values[0]
        AQI_High = rq['AQI_High'].values[0]
        index = rq['Index'].values[0]
        # Made By Kunsh Bhatia
        I = AQI_High - AQI_Low
        C = Conc_High - Conc_Low
        Diff = rq_values[i] - Conc_Low

        AQI_Conc = round(float((I / C) * Diff + AQI_Low))
        if int(AQI)>int(AQI_Conc):
            AQI_Pred_using_Params.append(AQI_Conc)
        else:
            pass
            
        if index == 1:
            color_codes_params.append(Color_Codes[0])
        elif index == 2:
            color_codes_params.append(Color_Codes[1])
        elif index == 3:
            color_codes_params.append(Color_Codes[2])
        elif index == 4:
            color_codes_params.append(Color_Codes[3])
        elif index == 5:
            color_codes_params.append(Color_Codes[4])
        elif index == 6:
            color_codes_params.append(Color_Codes[5])
        
    AQI_Pred = sorted(AQI_Pred_using_Params)[-1] # Highest value is considered as the AQI  
    return AQI_Pred,color_codes_params


# Made By Kunsh Bhatia
