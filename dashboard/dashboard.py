import streamlit as st
st.set_page_config(layout="wide")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")

# =========================
# LOAD DATA
# =========================

@st.cache_data
def load_data():
    return pd.read_csv("dashboard/main_data.csv")

df = load_data()

st.title("🚲 Bike Sharing Analysis Dashboard")
st.markdown("Dashboard interaktif untuk menganalisis pola penyewaan sepeda berdasarkan musim dan kondisi cuaca.")

# =========================
# SIDEBAR FILTER
# =========================

st.sidebar.header("🔎 Filter Data")

season_order = ["Spring", "Summer", "Fall", "Winter"]
weather_order = ["Clear", "Mist", "Light Snow/Rain", "Heavy Rain/Snow"]

selected_season = st.sidebar.multiselect(
    "Pilih Musim",
    options=season_order,
    default=season_order
)

selected_weather = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca",
    options=weather_order,
    default=weather_order
)

filtered_df = df[
    (df["season"].isin(selected_season)) &
    (df["weathersit"].isin(selected_weather))
]

if filtered_df.empty:
    st.warning("Data kosong setelah filter dipilih.")
else:

    # =========================
    # KPI SECTION
    # =========================

    st.subheader("📊 Ringkasan Utama")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Penyewaan",
        f"{int(filtered_df['cnt'].sum()):,}"
    )

    col2.metric(
        "Rata-rata Harian",
        f"{round(filtered_df['cnt'].mean(), 0):,}"
    )

    col3.metric(
        "Penyewaan Maksimum",
        f"{int(filtered_df['cnt'].max()):,}"
    )

    st.divider()

    # =========================
    # VISUALISASI
    # =========================

    col_left, col_right = st.columns(2)

    # ---- MUSIM ----
    with col_left:
        st.subheader("📅 Rata-rata Penyewaan per Musim")

        season_data = (
            filtered_df.groupby("season")["cnt"]
            .mean()
            .reindex(season_order)
            .dropna()
            .reset_index()
        )

        fig1, ax1 = plt.subplots(figsize=(6,4))
        sns.barplot(
            data=season_data,
            x="season",
            y="cnt",
            order=season_order,
            ax=ax1
        )
        ax1.set_xlabel("Musim")
        ax1.set_ylabel("Rata-rata Penyewaan")
        ax1.set_title("Penyewaan Berdasarkan Musim")
        st.pyplot(fig1)

    # ---- CUACA ----
    with col_right:
        st.subheader("🌤 Rata-rata Penyewaan per Cuaca")

        weather_data = (
            filtered_df.groupby("weathersit")["cnt"]
            .mean()
            .reindex(weather_order)
            .dropna()
            .reset_index()
        )

        fig2, ax2 = plt.subplots(figsize=(6,4))
        sns.barplot(
            data=weather_data,
            x="weathersit",
            y="cnt",
            order=weather_order,
            ax=ax2
        )
        ax2.set_xlabel("Kondisi Cuaca")
        ax2.set_ylabel("Rata-rata Penyewaan")
        ax2.set_title("Penyewaan Berdasarkan Cuaca")
        plt.xticks(rotation=25)
        st.pyplot(fig2)

    st.divider()

    # =========================
    # DATA PREVIEW (MINIMAL)
    # =========================

    with st.expander("Lihat Data (Preview)"):
        st.dataframe(filtered_df.head())
