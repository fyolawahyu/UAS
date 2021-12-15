import streamlit as st
import numpy as np
import pandas as pd
import json

st.title('oke')

# Read Data Json
with open ("kode_negara_lengkap.json") as f:
    kode_negara = json.load(f)

# Read Data CSV dan ubah ke data frame
csv = pd.read_csv("produksi_minyak_mentah.csv")
df = pd.DataFrame(csv)

# Mengubah string menjadi float pada data produksi
df['produksi'] = df['produksi'].astype(str).str.replace(".", "", regex=True).astype(float)
df['produksi'] = df['produksi'].astype(str).str.replace(",", "", regex=True).astype(float)
df['produksi'] = pd.to_numeric(df['produksi'], errors='coerce')

df2 = pd.DataFrame(df,columns= ['kode_negara','tahun','produksi'])
df2=df2.loc[df2['kode_negara']=='AUS']
df2['produksi'] = pd.to_numeric(df2['produksi'], errors='coerce')

st.write(df2)

df2 = pd.DataFrame(df,columns= ['kode_negara','tahun','produksi'])
df2=df2.loc[df2['tahun']==1971]
df2['produksi'] = pd.to_numeric(df2['produksi'], errors='coerce')

st.write(df2)

fig, ax = plt.subplots()
ax.plot(df['tahun'], df['produksi'], label = df['tahun'])
ax.set_title("T")
ax.set_xlabel("Tahun", fontsize = 12)
ax.set_ylabel("Jumlah Produksi", fontsize = 12)
ax.legend(fontsize = 7.8)
plt.show
