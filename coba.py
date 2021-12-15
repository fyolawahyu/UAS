import streamlit as st
import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt
from matplotlib import cm

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
