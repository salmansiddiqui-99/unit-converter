import streamlit as st

st.title ("UNIT Converter App")
st.markdown("### Converts Length, Weight And Time")
st.write("Welcome! Select a category")

category = st.selectbox("Choose ACategory", ["Lenght", "Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Lenght":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
        
    elif category == "Time":
        if unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        
if category == "Lenght":
    unit = st.selectbox("Select Conversation", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("Select Conversation", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("Select Conversation", ["Minutes to Seconds", "Seconds to Minutes", "Hours to Minutes", "Minutes to Hours"])

value = st.number_input("Enter the Value to Convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The Result Is {result: .3f}")

