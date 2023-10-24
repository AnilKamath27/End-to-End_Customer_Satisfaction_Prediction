import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title("Invistico Airline Customer Satisfaction Prediction")

# Create dropdowns for categorical features
gender = st.selectbox("Gender", ["Female", "Male"])
customer_type = st.selectbox("Customer Type", ["Loyal Customer", "Disloyal Customer"])
type_of_travel = st.selectbox("Type of Travel", ["Personal Travel", "Business travel"])
class_type = st.selectbox("Class", ["Eco", "Business", "Eco Plus"])

# Input fields for numerical features
age = st.number_input("Age")
flight_distance = st.number_input("Flight Distance")

# Create sliders for features with values between 0 and 5
seat_comfort = st.slider("Seat comfort", 0, 5)
departure_arrival_time = st.slider("Departure/Arrival time convenient", 0, 5)
food_and_drink = st.slider("Food and drink", 0, 5)
gate_location = st.slider("Gate location", 0, 5)
inflight_wifi_service = st.slider("Inflight wifi service", 0, 5)
inflight_entertainment = st.slider("Inflight entertainment", 0, 5)
online_support = st.slider("Online support", 0, 5)
online_booking = st.slider("Ease of Online booking", 0, 5)
on_board_service = st.slider("On-board service", 0, 5)
leg_room_service = st.slider("Leg room service", 0, 5)
baggage_handling = st.slider("Baggage handling", 0, 5)
checkin_service = st.slider("Checkin service", 0, 5)
cleanliness = st.slider("Cleanliness", 0, 5)
online_boarding = st.slider("Online boarding", 0, 5)

# Create a button to trigger the prediction
if st.button("Submit"):
    # Load the pre-trained model
    with open('XGBoost_Model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    data = {
        "Gender": gender,
        "Customer Type": customer_type,
        "Type of Travel": type_of_travel,
        "Class": class_type,
        "Age": age,
        "Flight Distance": flight_distance,
        "Seat comfort": seat_comfort,
        "Departure/Arrival time convenient": departure_arrival_time,
        "Food and drink": food_and_drink,
        "Gate location": gate_location,
        "Inflight wifi service": inflight_wifi_service,
        "Inflight entertainment": inflight_entertainment,
        "Online support": online_support,
        "Ease of Online booking": online_booking,
        "On-board service": on_board_service,
        "Leg room service": leg_room_service,
        "Baggage handling": baggage_handling,
        "Checkin service": checkin_service,
        "Cleanliness": cleanliness,
        "Online boarding": online_boarding,
        "Departure Delay in Minutes": 0,  
        "Arrival Delay in Minutes": 0,
    }


    input_data = pd.DataFrame(data, index=[0])
    prediction = model.predict(input_data)[0]
    class_labels = ["Unsatisfied Customer", "Satisfied Customer"]
    st.write("Prediction: ", class_labels[prediction])
