import streamlit as st
from joblib import load

st.title("Engine Condition Prediction")

rpm = st.number_input("Enter engine RPM Between 61 and 2239" , min_value = 61 , max_value = 2239)
Lub_oil_pressure = st.number_input("Enter engine Lub oil pressure between 0 and 7" , min_value = 0 , max_value = 7)
Fuel_pressure = st.number_input("Enter Fuel pressure between 0 and 21" , min_value = 0 , max_value = 21)
Coolant_pressure = st.number_input("Enter coolant pressure between 0 and 8" , min_value = 0 , max_value = 8)
Lub_oil_temp = st.number_input("Enter Lub oil temperature between 71 and 90" , min_value = 71 , max_value = 90)
Coolant_temp = st.number_input("Enter coolant temperature between 61 and 196" , min_value = 61 , max_value = 196)

clicked = st.button("Predict Engine Condition")

model = load('engine.joblib')

if(clicked == True):
    data = [rpm , Lub_oil_pressure , Fuel_pressure , Coolant_pressure , Lub_oil_temp , Coolant_temp]
    print(data)
    pred = model.predict([data])
    st.write(pred[0])
    print(pred[0])
    if(pred[0] == 0):
        st.header("Engine condition is Bad")
    else:
        st.header("Engine condition is good")