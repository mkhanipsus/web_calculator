import streamlit as st

st.title("🧮 Web Calculator")

# Input fields
a = st.number_input("Enter first number:")
b = st.number_input("Enter second number:")

# Select operation
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate result
if operation == "Add":
    result = a + b
elif operation == "Subtract":
    result = a - b
elif operation == "Multiply":
    result = a * b
elif operation == "Divide":
    result = a / b if b != 0 else "Cannot divide by zero"

# Display result
st.write("### Result:", result)
