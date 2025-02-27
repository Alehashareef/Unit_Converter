import streamlit as st

def convert_units(value, unit_from, unit_to):
    conversion_factors = {
        ('km', 'miles'): 0.621371,
        ('miles', 'km'): 1.60934,
        ('meters', 'feet'): 3.28084,
        ('feet', 'meters'): 0.3048,
        ('kg', 'pounds'): 2.20462,
        ('pounds', 'kg'): 0.453592,
        ('liters', 'gallons'): 0.264172,
        ('gallons', 'liters'): 3.78541,
        ('km', 'feet'): 3280.84,
        ('feet', 'km'): 0.0003048,
        ('celsius', 'fahrenheit'): lambda c: (c * 9/5) + 32,
        ('fahrenheit', 'celsius'): lambda f: (f - 32) * 5/9,
        ('seconds', 'minutes'): 1/60,
        ('minutes', 'seconds'): 60,
        ('minutes', 'hours'): 1/60,
        ('hours', 'minutes'): 60,
        ('square meters', 'square feet'): 10.764,
        ('square feet', 'square meters'): 0.092903
    }
    
    if unit_from == unit_to:
        return value
    
    conversion = conversion_factors.get((unit_from, unit_to), None)
    if callable(conversion):
        return conversion(value)
    return value * conversion if conversion else "Conversion not available"

# Streamlit App Title
st.title("🔄 :blue[Unit Converter]")
st.markdown("---")  # Adds a separator line

# Sidebar for Conversion Type Selection
st.sidebar.title("🔧 :blue[Choose a Category :]")
st.sidebar.markdown("🔄 Convert units quickly and accurately!")
category = st.sidebar.radio("", ["📏 Length", "⚖️ Weight", "🌡️ Temperature", "💧 Liquid", "⏳ Time", "📐 Area"], key="category")

# Select Units Based on Category
if category == "📏 Length":
    unit_from = st.selectbox("From:", ["km", "miles", "meters", "feet"], key="unit_from_length")
    unit_to = st.selectbox("To:", ["km", "miles", "meters", "feet"], key="unit_to_length")
elif category == "⚖️ Weight":
    unit_from = st.selectbox("From:", ["kg", "pounds"], key="unit_from_weight")
    unit_to = st.selectbox("To:", ["kg", "pounds"], key="unit_to_weight")
elif category == "🌡️ Temperature":
    unit_from = st.selectbox("From:", ["celsius", "fahrenheit"], key="unit_from_temp")
    unit_to = st.selectbox("To:", ["celsius", "fahrenheit"], key="unit_to_temp")
elif category == "💧 Liquid":
    unit_from = st.selectbox("From:", ["liters", "gallons"], key="unit_from_liquid")
    unit_to = st.selectbox("To:", ["liters", "gallons"], key="unit_to_liquid")
elif category == "⏳ Time":
    unit_from = st.selectbox("From:", ["seconds", "minutes", "hours"], key="unit_from_time")
    unit_to = st.selectbox("To:", ["seconds", "minutes", "hours"], key="unit_to_time")
elif category == "📐 Area":
    unit_from = st.selectbox("From:", ["square meters", "square feet"], key="unit_from_area")
    unit_to = st.selectbox("To:", ["square meters", "square feet"], key="unit_to_area")

# Input Value to Convert
value = st.number_input("Enter value:", min_value=0.0, format="%.2f", key="value")

# Convert Button
if st.button("Convert", key="convert_button"):
    result = convert_units(value, unit_from, unit_to)
    st.subheader(f"Result: {result} {unit_to}")

st.markdown("---")  # Adds a separator line
st.markdown(" 🚀**Aleha Shareef** |  Keep Growing & Learning!")