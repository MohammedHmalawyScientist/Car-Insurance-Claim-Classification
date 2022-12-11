import streamlit as st
import joblib
import sklearn
import catboost

st.title("Car Insurance Claim Classification")
st.write("This is a web app to predict whether a customer will claim the insurance or not")

gender = st.radio("Gender",["Male","Female"])
married = st.radio("Married",["Yes","No"])
vehicle_type = st.radio("Vehicle Type",["Sedan","Sports Car"])
vehicle_year = st.radio("Vehicle Year",["After 2015","Before 2015"])
education = st.selectbox("Education",["University","High School","None"])
income = st.selectbox("Income",["Upper Class","Middle Class","Working Class","Poverty"])
age = st.selectbox("Age",["16-25","26-39","40-64","65+"])
driving_experience = st.selectbox("Driving Experience",["0-9y","10-19y","20-29y","30y+"])
postal_code = st.selectbox("Postal Code",[10238,32765,92101,21217])
credit_score = st.number_input("Credit Score",0.00,1.00,step=0.01)

children = st.number_input("Children",0,10,step=1)
vehicle_ownership = st.number_input("Vehicle Ownership",0,100,step=1)
annual_mileage = st.number_input("Annual Mileage",0,100000,step=1000)
speeding_violations = st.number_input("Speeding Violations",0,100,step=1)
duis = st.number_input("Duis",0,100,step=1)
past_accidents = st.number_input("Past Accidents",0,100,step=1)

if gender == "Male":
    gender = 1
elif gender == "Female":
    gender = 0

if married == "Yes":
    married = 1
elif married == "No":
    married = 0

if vehicle_type == "Sedan":
    vehicle_type = 1
elif vehicle_type == "Sports Car":
    vehicle_type = 0

if vehicle_year == "After 2015":
    vehicle_year = 1
elif vehicle_year == "Before 2015":
    vehicle_year = 0

if income == "Upper Class":
    income = 3
elif income == "Middle Class":
    income = 2
elif income == "Working Class":
    income = 1
elif income == "Poverty":
    income = 0

if age == "16-25":
    age = 3
elif age == "26-39":
    age = 2
elif age == "40-64":
    age = 1
elif age == "65+":
    age = 0

if driving_experience == "0-9y":
    driving_experience = 3
elif driving_experience == "10-19y":
    driving_experience = 2
elif driving_experience == "20-29y":
    driving_experience = 1
elif driving_experience == "30y+":
    driving_experience = 0

def get_education(education):
    if education == "University":
        return [0,1]
    elif education == "High School":
        return [0,0]
    elif education == "None":
        return [1,0]

def get_postal_code(postal_code):
    if postal_code == 10238:
        return [0,0,0]
    elif postal_code == 32765:
        return [0,1,0]
    elif postal_code == 92101:
        return [0,0,1]
    elif postal_code == 21217:
        return [1,0,0]

def professionality(driving_experience, age):
    if driving_experience == 0:
        if age == 0 or age == 1:
            return 1
        else:
            return 0
    else:
        return 0

row_data = [age, gender, driving_experience, income, credit_score, vehicle_ownership, vehicle_year, married, children, annual_mileage, vehicle_type, speeding_violations, duis, past_accidents]
row_data.extend(get_education(education))
row_data.extend(get_postal_code(postal_code))
row_data.append(professionality(driving_experience, age))

model = joblib.load("model.h5")
scaler = joblib.load("scaler.h5")

if st.button("Predict"):
    prediction = model.predict(scaler.transform([row_data]))
    if prediction == 0:
        st.write("The customer will not claim the insurance")
        st.snow()
        st.success("Match found!")
    else:
        st.write("The customer will claim the insurance")
        st.snow()
        st.success("Match found!")