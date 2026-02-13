import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Bike Sharing Analysis Dashboard")

df = pd.read_csv("dashboard/main_data.csv")

menu = st.selectbox("Pilih Analisis", 
                    ["Musim", "Cuaca", "Hari Kerja"])

# =========================
# ANALISIS MUSIM
# =========================
if menu == "Musim":
    st.subheader("Analisis Rata-rata Penyewaan Berdasarkan Musim")
    st.write("Visualisasi ini menunjukkan perbandingan rata-rata jumlah penyewaan sepeda pada setiap musim.")

    data = df.groupby("season")["cnt"].mean().reset_index()

    fig, ax = plt.subplots()
    sns.barplot(data=data, x="season", y="cnt", ax=ax)
    ax.set_xlabel("Musim")
    ax.set_ylabel("Rata-rata Penyewaan")
    st.pyplot(fig)

    st.info("Insight: Musim dengan rata-rata penyewaan tertinggi dapat menjadi periode optimal untuk peningkatan armada dan strategi promosi.")

# =========================
# ANALISIS CUACA
# =========================
elif menu == "Cuaca":
    st.subheader("Analisis Rata-rata Penyewaan Berdasarkan Kondisi Cuaca")
    st.write("Visualisasi ini menunjukkan pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda.")

    data = df.groupby("weathersit")["cnt"].mean().reset_index()

    fig, ax = plt.subplots()
    sns.barplot(data=data, x="weathersit", y="cnt", ax=ax)
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Rata-rata Penyewaan")
    plt.xticks(rotation=30)
    st.pyplot(fig)

    st.info("Insight: Cuaca cerah cenderung meningkatkan jumlah penyewaan dibandingkan kondisi hujan atau bersalju.")

# =========================
# ANALISIS HARI KERJA
# =========================
else:
    st.subheader("Perbandingan Penyewaan: Hari Kerja vs Akhir Pekan")
    st.write("Visualisasi ini membandingkan rata-rata penyewaan sepeda antara hari kerja dan akhir pekan/libur.")

    # Ubah label supaya lebih manusiawi
    df["workingday_label"] = df["workingday"].map({
        0: "Weekend / Holiday",
        1: "Working Day"
    })

    data = df.groupby("workingday_label")["cnt"].mean().reset_index()

    fig, ax = plt.subplots()
    sns.barplot(data=data, x="workingday_label", y="cnt", ax=ax)
    ax.set_xlabel("Kategori Hari")
    ax.set_ylabel("Rata-rata Penyewaan")
    st.pyplot(fig)

    st.info("Insight: Pola penyewaan pada hari kerja cenderung lebih stabil dibandingkan akhir pekan.")
