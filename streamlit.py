import streamlit as st
from Python_Programs.backend_processing import main_function,color_code_AQI,Precautions
from Python_Programs.AQI_Calc_Using_Params import AQI_Using_Params
import datetime  
  
st.set_page_config(
    page_icon="🌇", 
    page_title="DTU AQI Predictor",
    layout = "wide"
)
# Made By Kunsh Bhatia
st.markdown(f"""
        <div style="background-color: #CFE1E3; padding: 30px; margin-top: 20px;
                border-radius: 15px; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
            <div style="font-size: 35px; font-weight: bold; color:#2BD935 ;">DTU Air Quality Predictor 🌍 </div>
        </div>
        """, unsafe_allow_html=True)
st.write("")
with st.form("AQI Prediction"):
    selected_date = st.date_input("Choose a date", value=datetime.date.today(), format="DD/MM/YYYY")
    Date = selected_date.day
    Month = selected_date.month
    Year = selected_date.year

    submitted = st.form_submit_button("Submit")

if submitted:
    AQI, PM25, PM10, NO2, SO2, CO, O3, Grade = main_function(Date, Month, Year)

    AQI_Param,color_code_params = AQI_Using_Params(Date, Month, Year)

    if (AQI_Param - int(AQI)) < 50:
         AQI_Param = AQI_Param - 41 #MAE for AQI is nearly 41 . Hence if values are really close , choosing the MAE , so chances of error becomes min.
    else:
         AQI_Param = AQI_Param

    # Ranging the values using their respective Mean Absolute Error(s)
    final_AQI = f"{(AQI_Param)} - {int(AQI) + 40 }"
    final_PM25 = f"{max(0, round(PM25 - 58.47, 2))} - {round(PM25 + 58.47, 2)}"
    final_PM10 = f"{max(0, round(PM10 - 105, 2))} - {round(PM10 + 105, 2)}" ### All these mathematical operations are done after testing the model with real world scenarios .
    final_NO2 = f"{max(0, round(NO2 - 30, 2))} - {round(NO2 + 30, 2)}"
    final_SO2 = f"{max(0, round(SO2 - 30, 2))} - {round(SO2 + 30 , 2)}"
    final_CO = f"{max(0, round(CO - 0.30, 2))} - {round(CO + 0.7, 2)}"
    final_O3 = f"{max(0, round(O3 - 19, 2))} - {round(O3 + 35, 2)}"
    AQI_Color_Codes = color_code_AQI(AQI)
    Precaution = Precautions(AQI)
# Made By Kunsh Bhatia
    def info_card(title, value, icon, unit="", color_code="#0072C6", information_about_pollutant=""):
        st.markdown(f"""
            <div title="{information_about_pollutant}"
                 style="background-color: #f0f2f6; padding: 20px; margin-bottom: 10px; margin-top: 5px; 
                        border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); text-align: center; cursor: help;">
                <div style="font-size: 30px;">{icon}</div>
                <div style="font-size: 27px; font-weight: bold; margin-top: 5px;">{title}</div>
                <div style="font-size: 25px; font-weight: bold; color: {color_code};">{value}</div>
                <div style="font-size: 14px; color: #0072C6;">{unit}</div>
            </div>
        """, unsafe_allow_html=True)

    info_pollutant = [
        """ - PM2.5 are very tiny particles in air.
            - They go deep into the lungs and can enter the blood. 
            - They cause breathing problems, asthma etc.""",
        """ - PM10 are bigger dust particles than PM2.5.
            - They irritate nose, throat, and lungs. 
            - Main sources are road dust, construction, and industries.""",
        """ - NO₂ is mainly released from vehicles and power plants.
            - It irritates lungs and reduces breathing capacity. 
            - Long exposure increases asthma and lung infections.""",
        """ - SO₂ comes from burning coal and oil in industries.
            - It causes throat irritation and breathing discomfort.
            - It also leads to acid rain which harms crops and water.""",
        """ - CO is a colorless and odorless gas from incomplete burning.
            - It reduces oxygen supply in the blood.
            - High levels can cause headache, dizziness etc.""",
        """ - Ground level ozone forms due to sunlight and pollutants.
            - It causes chest pain, coughing, and eye irritation.
            - It also damages crops and plants."""]    

    st.markdown(f"""
        <div style="background-color: #e0f7da; padding: 30px; margin-top: 20px;
                border-radius: 15px; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
            <div style="font-size: 20px; font-weight: bold;">Predicted AQI For</div>
            <div style="font-size: 25px; font-weight: bold; color:#573FD1 ;">{Date}/{Month}/{Year}</div>
            <div style="font-size: 42px; font-weight: bold; color: {AQI_Color_Codes}; margin-top: 15px;">{final_AQI}</div>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        info_card("PM 2.5", final_PM25, "🌫️", "µg/m^3",color_code_params[0],info_pollutant[0])
    with col2: # Made By Kunsh Bhatia
        info_card("PM 10", final_PM10, "🏭", "µg/m^3",color_code_params[1],info_pollutant[1])
    with col3:
        info_card("NO2", final_NO2, "🚗", "µg/m^3",color_code_params[2],info_pollutant[2])

    col4, col5, col6 = st.columns(3)
    with col4:
        info_card("SO2", final_SO2, "🔋", "µg/m^3",color_code_params[3],info_pollutant[3])
    with col5:
        info_card("CO", final_CO, "♨️", "mg/m^3",color_code_params[4],info_pollutant[4])
    with col6:
        info_card("Ozone", final_O3, "🌐", "µg/m^3",color_code_params[5],info_pollutant[5])

    st.markdown(f"""
        <div style="background-color: #e0f7da; padding: 30px; margin-top: 20px;
                border-radius: 15px; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
            <div style="font-size: 20px; font-weight: bold;">Overall Air Quality </div>
            <div style="font-size: 42px; font-weight: bold; color: {AQI_Color_Codes}; margin-top: 15px;">{Grade}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div style="background-color: #e0f7da; padding: 30px; margin-top: 20px;
                border-radius: 15px; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
            <div style="font-size: 30px; font-weight: bold; color: #1C9CD9;">PRECAUTIONS ⛅ </div>
            <div style="font-size: 20px; font-weight: bold; color: #000000; margin-top: 15px;">{Precaution[0]}</div>
            <div style="font-size: 20px; font-weight: bold; color: #000000; margin-top: 15px;">{Precaution[1]}</div>
            <div style="font-size: 20px; font-weight: bold; color: #000000; margin-top: 15px;">{Precaution[2]}</div>
            <div style="font-size: 20px; font-weight: bold; color: #000000; margin-top: 15px;">{Precaution[3]}</div>
            <div style="font-size: 20px; font-weight: bold; color: #000000; margin-top: 15px;">{Precaution[4]}</div>
        </div>
        """, unsafe_allow_html=True)
    # Made By Kunsh Bhatia
    st.write("")
    with st.expander("📊 Symbologies"):
        st.markdown("""
| Color | Category | Health Concern Level | Meaning / Public Advisory |
|:------|:-----------|:---------------------|:--------------------------|
| 🟩 | **Good** | ✅ *Minimal or no risk* | Air quality is considered satisfactory; air pollution poses little or no risk. |
| 🟨 | **Satisfactory** | ⚠️ *Acceptable but some pollutants may affect sensitive people* | Air quality is acceptable; however, there may be a moderate health concern for a small number of unusually sensitive people. |
| 🟧 | **Moderate** | 🧑‍⚕️ *Risk to people with heart/lung disease, children, older adults* | Members of sensitive groups may experience health effects; the general public is not likely to be affected. |
| 🟥 | **Poor** | 🚨 *Everyone may begin to experience health effects* | Some members of the general public may experience health effects; members of sensitive groups may experience more serious effects. |
| 🟪 | **Very Unhealthy/Severe** | ☣️ *Health alert: everyone may experience serious effects* | Health warnings of emergency conditions; the entire population is more likely to be affected. |
    """, unsafe_allow_html=True)

    with st.expander("📄 Which Dataset is used to train the model?"):
        st.markdown("""
            You may find all the files of the dataset used to train the model below :-

            - https://www.kaggle.com/datasets/kunshbhatia/delhi-air-quality-dataset
            - The above mentioned dataset is taken from CPCB's official website .
        """)
    with st.expander("📄 Terms & Conditions "):
        st.markdown("""
            Last updated: July 25, 2025
            - **Informational Use Only :** This model is for educational and informational purposes only , NOT for medical or emergency decisions.
            - **No Real-Time Guarantee:** Predictions are based on past data (2021-2024) and may not match official real time AQI reports.
            - **No Liability:** The developer is not responsible for any actions taken based on the model's output.
            - **Data Source:** Dataset(s) are sourced from publicly available platforms like CPCB,SBCB etc.
            - **Ownership:** All code and logic are original. Reuse or distribution without permission is prohibited ⚠️.
        """)

st.markdown("""
    <hr style="margin-top: 2rem; margin-bottom: 0;">
    <div style="text-align: center; color: grey; font-size: 14px; padding: 10px 0;">
        Disclaimer : The data is taken from CPCB's official website and the model is trained using DTU and Bawana's dataset(s).
    </div>
    <div style="text-align: center; color: grey; font-size: 14px; padding: 10px 0;">
        © 2025 Kunsh Bhatia | Built with ❤️ and ☕
    </div>
""", unsafe_allow_html=True)



# Made By Kunsh Bhatia
