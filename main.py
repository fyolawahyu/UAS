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

#--Poin (a)--
df_ = ch_.dataFrame
df_info = jh_.dataFrame
negara_li = df_info['name'].tolist()

negara = st.selectbox('Pilih negara : ',negara_li) 


kode = df_info[df_info['name']==negara]['alpha-3'].tolist()[0]


st.write('Kode negara : ',kode)
st.write('Negara : ',negara)

# Mengubah string menjadi float pada data produksi
df['produksi'] = df['produksi'].astype(str).str.replace(".", "", regex=True).astype(float)
df['produksi'] = df['produksi'].astype(str).str.replace(",", "", regex=True).astype(float)
df['produksi'] = pd.to_numeric(df['produksi'], errors='coerce')

df2 = pd.DataFrame(df,columns= ['negara','tahun','produksi'])
df2=df2.loc[df2['negara']]
df2['produksi'] = pd.to_numeric(df2['produksi'], errors='coerce')

st.write(df2)




