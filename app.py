import streamlit as st
import pandas as pd
import joblib

model_data = joblib.load("air_quality_model.pkl")
model = model_data["model"]
feature_columns = model_data["feature_columns"]
anomaly_threshold = joblib.load("anomaly_threshold.pkl")

st.set_page_config(
    page_title="Air Quality Prediction System",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Air Quality Prediction System")
st.write("Estimate PM2.5 concentration and identify unusually high pollution readings.")
st.info(
    "Enter environmental measurements to estimate PM2.5 concentration and assess pollution levels."
)

wind_directions = ["E", "ENE", "ESE", "N", "NE", "NNE", "NNW", "NW", "S", "SE", "SSE", "SSW", "SW", "W", "WNW", "WSW"]
stations = ["Aotizhongxin", "Changping", "Dingling", "Dongsi", "Guanyuan", "Gucheng", 
            "Huairou", "Nongzhanguan", "Shunyi", "Tiantan", "Wanliu", "Wanshouxigong"]

tab1, tab2 = st.tabs([
    "PM2.5 Prediction",
    "Pollution Anomaly Detection"
])

with tab1:
    st.header("Predict PM2.5 Concentration")
    st.write("Enter the pollutant and weather measurements below.")

    with st.form("prediction_form"):
        st.subheader("Pollutant Measurements")
        col1, col2, col3 = st.columns(3)

        with col1:
            pm10 = st.number_input("PM10 (µg/m³)", min_value=0.0, value=100.0)
            so2 = st.number_input("SO2 (µg/m³)", min_value=0.0, value=10.0)
        with col2:
            no2 = st.number_input("NO2 (µg/m³)", min_value=0.0, value=40.0)
            co = st.number_input("CO (mg/m³)", min_value=0.0, value=1.0)
        with col3:
            o3 = st.number_input("O3 (µg/m³)", min_value=0.0, value=60.0)

        st.subheader("Weather Measurements")
        col1, col2, col3 = st.columns(3)

        with col1:
            temp = st.number_input("Temperature (°C)", value=15.0)
            pres = st.number_input("Pressure (hPa)", value=1010.0)
        with col2:
            dewp = st.number_input("Dew Point (°C)", value=5.0)
            rain = st.number_input("Rainfall (mm)", min_value=0.0, value=0.0)
        with col3:
            wspm = st.number_input("Wind Speed (m/s)", min_value=0.0, value=1.0)
            wd = st.selectbox("Wind Direction", wind_directions)

        st.subheader("Time and Monitoring Station")
        col1, col2, col3 = st.columns(3)

        with col1:
            month = st.selectbox("Month", list(range(1, 13)), index=0)
        with col2:
            hour = st.selectbox("Hour", list(range(24)), index=12)
        with col3:
            station = st.selectbox("Monitoring Station", stations)

        predict_button = st.form_submit_button("Predict PM2.5", type="primary")

    if predict_button:
        input_data = pd.DataFrame(
            0,
            index=[0],
            columns=feature_columns
        )

        input_values = {
            "PM10": pm10,
            "SO2": so2,
            "NO2": no2,
            "CO": co,
            "O3": o3,
            "TEMP": temp,
            "PRES": pres,
            "DEWP": dewp,
            "RAIN": rain,
            "WSPM": wspm,
            "month": month,
            "hour": hour
        }

        for feature, value in input_values.items():
            input_data.at[0, feature] = value

        wind_column = "wd_" + wd
        station_column = "station_" + station

        if wind_column in input_data.columns:
            input_data.at[0, wind_column] = 1

        if station_column in input_data.columns:
            input_data.at[0, station_column] = 1

        prediction = model.predict(input_data)[0]

        st.success("PM2.5 prediction completed!")

        st.metric(
            label="Predicted PM2.5 Concentration",
            value=f"{prediction:.2f} µg/m³"
        )
        st.caption(
            "This is an estimate based on the values you entered, "
            "not a live air-quality measurement."
        )

with tab2:

    st.header("Pollution Anomaly Detection")
    st.write(
        "You can enter a PM2.5 reading to check whether it exceeds the statistical high-pollution threshold identified using the IQR method."
    )

    pm25_value = st.number_input(
        "Enter PM2.5 Reading (µg/m³)",
        min_value=0.0,
        value=100.0,
        key="anomaly_input"
    )

    if st.button("Check Pollution Level", type="primary"):
        if pm25_value > anomaly_threshold:
            st.error(
                "High-pollution anomaly detected! "
                "This reading is unusually high compared with the dataset distribution."
            )
        else:
            st.success(
                "No high-pollution anomaly detected according to the IQR threshold."
            )

        st.write(f"Entered PM2.5 reading: **{pm25_value:.2f} µg/m³**")
