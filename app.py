import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("model.pkl",'rb'))

st.title("Penguin Species Predictor")

bill_l = st.slider("Bill Length", 30.0,60.0,40.0)
bill_d = st.slider("Bill Depth", 12.0,22.0,15.0)
filpper_l = st.slider("Flipper Length", 160,250,190)
body_mass = st.slider("Body Mass", 2700,6500,3500)

if st.button("Predict"):
    data = np.array([[bill_l,bill_d,filpper_l,body_mass]])
    prediction = model.predict(data)
    st.success(f'Species : {prediction[0]}')