#IMPORT AWAL
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm 
import streamlit as st
from fileHandler import csvHandler,jsonHandler

#READ DATA JSON
with open("kode_negara_lengkap.json", "r") as read_file:
    data = json.load(read_file)
# for i in data:
#     print(type(i))
print(data[0])
dfJ = pd.DataFrame(data)


#READ DATA CSV
csv = pd.read_csv("produksi_minyak_mentah.csv")
df = pd.DataFrame(csv)
print(df)

st.title('Data Produksi Minyak Mentah')
st.header('UAS Pemrograman Komputer')
ch_ = csvHandler('produksi_minyak_mentah.csv')
jh_ = jsonHandler('kode_negara_lengkap.json')

st.sidebar.title("Pengaturan")
left_col, mid_col, right_col = st.columns(3)

# Mengubah string menjadi float pada data produksi
df['produksi'] = df['produksi'].astype(str).str.replace(".", "", regex=True).astype(float)
df['produksi'] = df['produksi'].astype(str).str.replace(",", "", regex=True).astype(float)
df['produksi'] = pd.to_numeric(df['produksi'], errors='coerce')

df2 = pd.DataFrame(df,columns= ['kode_negara','tahun','produksi'])
df2=df2.loc[df2['kode_negara']=="AUS"]
df2['produksi'] = pd.to_numeric(df2['produksi'], errors='coerce')

left_col.markdown(df2)

fig, ax = plt.subplots()
ax.plot(df2['tahun'], df2['produksi'], label = df2['tahun'])
ax.set_title("Jumlah produksi per bulan")
ax.set_xlabel("Tahun", fontsize = 12)
ax.set_ylabel("Jumlah Produksi", fontsize = 12)
ax.legend(fontsize = 2)
plt.show
right_col.pyplot(fig)

