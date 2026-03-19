import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title("Iris Flower Prediction 🌸")

# Inputs
sepal_length = st.slider("Sepal Length", 4.0, 8.0)
sepal_width = st.slider("Sepal Width", 2.0, 4.5)
petal_length = st.slider("Petal Length", 1.0, 7.0)
petal_width = st.slider("Petal Width", 0.1, 2.5)

# Prediction
if st.button("Predict"):
    if sepal_length != 0 and sepal_width != 0 and petal_length != 0 and petal_width != 0:
        data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = model.predict(data)
        st.success(f"Prediction: {prediction[0]}")
    else:
        st.warning("Please enter all values")