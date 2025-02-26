import streamlit as st

# Page configuration
st.set_page_config(page_title="Unit Converter", page_icon="🔢")

st.title("Unit Converter")
st.caption("Welcome to the Unit Converter!")

# Unit conversion dictionary (all values in meters)
conversion_factors = {
    "Kilometer": 1000,
    "Meter": 1,
    "Centimeter": 0.01,
    "Millimeter": 0.001,
    "Micrometer": 1e-6,
    "Nanometer": 1e-9,
    "Mile": 1609.34,
    "Yard": 0.9144,
    "Foot": 0.3048,
    "Inch": 0.0254,
    "Nautical Mile": 1852,
}

# User input
value = st.number_input("Enter the value to be converted")
from_unit = st.selectbox("Select the unit to convert from", conversion_factors.keys())
to_unit = st.selectbox("Select the unit to convert to", conversion_factors.keys())

# Conversion logic
if st.button("Convert"):
    if from_unit and to_unit:
        converted_value = (value * conversion_factors[from_unit]) / conversion_factors[to_unit]
        st.success(f"{value} {from_unit} is equal to {round(converted_value,4)} {to_unit}")
        st.balloons()  # Celebratory effect



st.write('-------------------------------------------------')
st.caption('©️ 2025 Unit Converter By Qirat Saeed. All rights reserved.')   
