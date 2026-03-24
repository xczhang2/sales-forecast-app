
import streamlit as st
import joblib
import numpy as np

model = joblib.load("sales_model.pkl")

st.title("売上予測アプリ")

temp = st.number_input("気温を入力", 0, 40, 20)
ad = st.number_input("広告費を入力", 0, 100000, 10000)

if st.button("予測する"):
    X = np.array([[temp, ad]])
    pred = model.predict(X)
    st.write(f"予測売上：{int(pred[0])} 円")
