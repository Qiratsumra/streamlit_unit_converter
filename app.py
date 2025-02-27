import streamlit as st

# Distance Converter Function (fixed unit names to match UI)
def distance_converter(from_unit, to_unit, value):
    units = {
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
    return value * units[from_unit] / units[to_unit]

# Temperature Converter Function (unchanged, correct)
def temperature_converter(from_unit, to_unit, value):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        result = (value - 32) * 5/9
    else:
        result = value
    return result

# Weight Converter Function (unchanged, correct)
def weight_converter(from_unit, to_unit, value):
    units = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
    }
    return value * units[from_unit] / units[to_unit]

# Pressure Converter Function (unchanged, correct)
def pressure_converter(from_unit, to_unit, value):
    units = {
        "Pascals": 1,
        "Hectopascals": 100,
        "Kilopascals": 1000,
        "Bar": 100000,
    }
    return value * units[from_unit] / units[to_unit]

# Streamlit UI (fixed distance unit options)
st.set_page_config(page_title='Unit Converter', page_icon='🔢')
st.title("Unit Converter")

category = st.selectbox("Select Category", ["Distance", "Temperature", "Weight", "Pressure"])

if category == "Distance":
    # Fixed unit names to match dictionary keys
    units = ["Kilometer", "Meter", "Centimeter", "Millimeter", 
            "Micrometer", "Nanometer", "Mile", "Yard", 
            "Foot", "Inch", "Nautical Mile"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter Value")
    result = distance_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

elif category == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit"])
    value = st.number_input("Enter Value")
    result = temperature_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

elif category == "Weight":
    from_unit = st.selectbox("From", ["Kilograms", "Grams", "Pounds", "Ounces"])
    to_unit = st.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces"])
    value = st.number_input("Enter Value")
    result = weight_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

elif category == "Pressure":
    from_unit = st.selectbox("From", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
    to_unit = st.selectbox("To", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
    value = st.number_input("Enter Value")
    result = pressure_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

st.write('-------------------------------------------------')
st.caption('©️ 2025 Unit Converter By Qirat Saeed. All rights reserved.')