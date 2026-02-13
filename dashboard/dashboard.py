import streamlit as st

st.set_page_config(layout="wide")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Bike Sharing Analysis Dashboard")

df = pd.read_csv("dashboard/main_data.csv")

# =========================
# SIDEBAR FILTER (INTERAKTIF)
# =========================
st.sidebar.header("Filter Data")

selected_season = st.sidebar.multiselect(
    "Pilih Musim",
    options=df["season"].unique(),
    default=df["season"].unique()
)

selected_weather = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca",
    options=df["weathersit"].unique(),
    default=df["weathersit"].unique()
)

filtered_df = df[
    (df["season"].isin(selected_season)) &
    (df["weathersit"].isin(selected_weather))
]

st.write("Data setelah filter:")
st.dataframe(filtered_df.head())

# =========================
# VISUALISASI
# =========================

st.subheader("Rata-rata Penyewaan Berdasarkan Musim")
season_data = filtered_df.groupby("season")["cnt"].mean().reset_index()

fig1, ax1 = plt.subplots()
sns.barplot(data=season_data, x="season", y="cnt", ax=ax1)
ax1.set_ylabel("Rata-rata Penyewaan")
st.pyplot(fig1)

st.subheader("Rata-rata Penyewaan Berdasarkan Cuaca")
weather_data = filtered_df.groupby("weathersit")["cnt"].mean().reset_index()

fig2, ax2 = plt.subplots()
sns.barplot(data=weather_data, x="weathersit", y="cnt", ax=ax2)
plt.xticks(rotation=30)
st.pyplot(fig2)
