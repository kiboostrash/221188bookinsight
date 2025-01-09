import streamlit as st
from scripts.data_processing import load_data

# Path ke dataset
DATA_PATH = "data/Book1.csv"

# Judul aplikasi
st.title("Aplikasi Analisis Data dengan Streamlit")

# Load data
data = load_data(DATA_PATH)

# Tampilkan data
if data is not None:
    st.subheader("Dataset")
    st.write(data.head())

    # Visualisasi data (contoh)
    st.subheader("Deskripsi Data")
    st.write(data.describe())
else:
    st.error("Data tidak ditemukan atau gagal dimuat.")
