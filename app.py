import streamlit as st, joblib, numpy as np

model = joblib.load("model.joblib")
st.title("House Price Predictor + GST/HST Checker")

area = st.number_input("GrLivArea", 1200)
lot = st.number_input("LotArea", 5000)
qual = st.slider("OverallQual", 1, 10, 5)

if st.button("Predict"):
    price = model.predict(np.array([[area, lot, qual]]))[0]
    st.success(f"Estimated Price: ${price:,.2f}")
    st.info("No GST/HST") if price < 1_000_000 else st.warning("🔴 GST/HST May Apply")
