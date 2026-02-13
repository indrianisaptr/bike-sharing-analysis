import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Bike Sharing Analysis Dashboard")

df = pd.read_csv("dashboard/main_data.csv")

menu = st.selectbox("Pilih Analisis", 
                    ["Musim", "Cuaca", "Hari Kerja"])

if menu == "Musim":
    data = df.groupby("season")["cnt"].mean().reset_index()
    fig, ax = plt.subplots()
    sns.barplot(data=data, x="season", y="cnt", ax=ax)
    st.pyplot(fig)

elif menu == "Cuaca":
    data = df.groupby("weathersit")["cnt"].mean().reset_index()
    fig, ax = plt.subplots()
    sns.barplot(data=data, x="weathersit", y="cnt", ax=ax)
    st.pyplot(fig)

else:
    data = df.groupby("workingday")["cnt"].mean().reset_index()
    fig, ax = plt.subplots()
    sns.barplot(data=data, x="workingday", y="cnt", ax=ax)
    st.pyplot(fig)
