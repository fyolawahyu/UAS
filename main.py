#UAS PEMROGRAMAN KOMPUTER
#FYOLA WAHYU KANAYA SALSABILA
#12220031

#IMPORT AWAL
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm 
import streamlit as st
from file import csv_,json_
from PIL import Image

#IMPORT GAMBAR
st.sidebar.title("Tentang")
st.sidebar.write('Dibuat Oleh : Fyola Wahyu K S - 12220031') 
image = Image.open('165420.jpg')
st.sidebar.image(image)

#READ DATA JSON
with open("kode_negara_lengkap.json", "r") as FileRead:
    jsonRead_1 = json.load(FileRead)
# for i in data:
#     print(type(i))
print(jsonRead_1[0])
dfJ_1 = pd.DataFrame(jsonRead_1)

#READ DATA CSV
csvRead_1 = pd.read_csv("produksi_minyak_mentah.csv")
dfC_1 = pd.DataFrame(csvRead_1)
print(dfC_1)

#OUTPUT JUDUL DAN HEADER
st.title('Analisis Data Produksi Minyak Mentah')
st.header('UAS Pemrograman Komputer')

#MEMBUAT DATA FRAME TIAP FILE
csvRead_2 = csv_('produksi_minyak_mentah.csv')
jsonRead_2 = json_('kode_negara_lengkap.json')
dfC_2 = csvRead_2.dataFrame
dfJ_2 = jsonRead_2.dataFrame
lst_negara = dfJ_2['name'].tolist()

lst_codeNegara = []
for i in list(dfC_2['kode_negara']) :
    if i not in list(dfJ_2['alpha-3']) :
        lst_codeNegara.append(i)

for i in lst_codeNegara :
    dfC_2 = dfC_2[dfC_2.kode_negara != i]
print(dfC_2)

#MENGATUR LETAK OUTPUT
st.sidebar.title("Pengaturan")
st.sidebar.header('Pengaturan Jumlah Produksi Per Bulan')


#--a---

left_col, right_col = st.columns(2)
left_col.write("Data Produksi Negara Pilihan")
negara = st.sidebar.selectbox('Pilih negara : ',lst_negara) 

kode = dfJ_2[dfJ_2['name']==negara]['alpha-3'].tolist()[0]

st.sidebar.write('Kode negara : ',kode)
st.sidebar.write('Negara : ',negara)

# MENGUBAH STRING MENJADI FLOAT
dfC_1['produksi'] = dfC_1['produksi'].astype(str).str.replace(".", "", regex=True).astype(float)
dfC_1['produksi'] =dfC_1['produksi'].astype(str).str.replace(",", "", regex=True).astype(float)
dfC_1['produksi'] = pd.to_numeric(dfC_1['produksi'], errors='coerce')

#OUTPUT TABEL A
df2 = pd.DataFrame(dfC_1,columns= ['kode_negara','tahun','produksi'])
df2=df2.loc[df2['kode_negara']==kode]
df2['produksi'] = pd.to_numeric(df2['produksi'], errors='coerce')

left_col.write(df2)

#OUTPUT GRAFIK A
fig, ax = plt.subplots()
ax.plot(df2['tahun'], df2['produksi'], label = df2['tahun'], color='orange')
ax.set_title("Jumlah Produksi Per Tahun di Negara Pilihan")
ax.set_xlabel("Tahun", fontsize = 12)
ax.set_ylabel("Jumlah Produksi", fontsize = 12)
ax.legend(fontsize = 2)
plt.show()
right_col.pyplot(fig)

#--b--
lcol, rcol = st.columns(2)
lcol.write('Negara dengan Produksi Terbesar')
st.sidebar.header('Pengaturan Negara dengan Data Produksi dan Kumulatif Terbesar')
tahun = st.sidebar.slider("Pilih Tahun produksi", min_value=1971, max_value=2015)
n = st.sidebar.slider("Pilih Banyak Negara", min_value=1, max_value=None)

dfb = dfC_2.loc[dfC_2['tahun'] == tahun]
dfb = dfb.sort_values(by='produksi', ascending = False)
dfbaru = dfb[:n]
lcol.write(dfbaru)

dfbaru.plot.bar(x='kode_negara', y='produksi')
plt.show()
rcol.pyplot(plt)

#--c--
lc, rc = st.columns(2)
lc.write('Negara dengan Produksi Kumulatif Terbesar')
list_a = []
kumulatif = []

for i in list (dfC_2['kode_negara']) :
    if i not in list_a:
        list_a.append(i)
        
for i in list_a :
    a=dfC_2.loc[dfC_2['kode_negara'] ==i,'produksi'].sum()
    kumulatif.append(a)
    
dk = pd.DataFrame(list(zip(list_a,kumulatif)), columns = ['kode_negara','kumulatif'])
dk = dk.sort_values(by=['kumulatif'], ascending = False)
dk2 = dk.sort_values(by=['kumulatif'], ascending = True)
dk1 = dk[:n]

lc.write(dk1)
dk1.plot.bar(x='kode_negara', y='kumulatif') 
plt.show()
rc.pyplot(plt)

#--d--
c1, c2, c3, c4 = st.columns(4)
col1, col2, col3, col4 = st.columns(4)

#bagian 1
jumlahProduksi = dfb[:1].iloc[0]['produksi']
kode_negara = dfb[:1].iloc[0]['kode_negara']
namaNegara = ""
regionNegara = ""
subregionNegara = ""

for i in range(len(dfJ_2)):
    if list(dfJ_2['alpha-3'])[i]==kode_negara:
        namaNegara = list(dfJ_2['name'])[i]
        regionNegara = list(dfJ_2['region'])[i]
        subregionNegara = list(dfJ_2['sub-region'])[i]
        
c1.write('Negara dengan Produksi Terbesar')
col1.write(jumlahProduksi)
col1.write(kode_negara)
col1.write(namaNegara)
col1.write(regionNegara)
col1.write(subregionNegara)

jumlahProduksi = dk[:1].iloc[0]['kumulatif']
kode_negara = dk[:1].iloc[0]['kode_negara']
namaNegara = ""
regionNegara = ""
subregionNegara = ""

for i in range(len(dfJ_2)):
    if list(dfJ_2['alpha-3'])[i]==kode_negara:
        namaNegara = list(dfJ_2['name'])[i]
        regionNegara = list(dfJ_2['region'])[i]
        subregionNegara = list(dfJ_2['sub-region'])[i]
        
c2.write('Negara dengan Produksi Terbesar pada Keseluruhan Tahun')
col2.write(jumlahProduksi)
col2.write(kode_negara)
col2.write(namaNegara)
col2.write(regionNegara)
col2.write(subregionNegara)


#bagian 2
dfterkecil = dfb[dfb.produksi !=0]
dfterkecil = dfterkecil.sort_values(by=['produksi'],ascending=True)
jumlahProduksi = dfterkecil[:1].iloc[0]['produksi']
kode_negara = dfterkecil[:1].iloc[0]['kode_negara']
namaNegara = ""
regionNegara = ""
subregionNegara = ""
                                    
for i in range(len(dfJ_2)):
    if list(dfJ_2['alpha-3'])[i]==kode_negara:
        namaNegara = list(dfJ_2['name'])[i]
        regionNegara = list(dfJ_2['region'])[i]
        subregionNegara = list(dfJ_2['sub-region'])[i]
                                    
c3.write('Negara dengan Produksi Terkecil')
col3.write(jumlahProduksi)
col3.write(kode_negara)
col3.write(namaNegara)
col3.write(regionNegara)
col3.write(subregionNegara)

dfakumulatifmin=dk2[dk2.kumulatif !=0]
dfakumulatifmin = dfakumulatifmin[:1].sort_values(by=['kumulatif'], ascending = True)
jumlahProduksi = dfakumulatifmin[:1].iloc[0]['kumulatif']
kode_negara = dfakumulatifmin[:1].iloc[0]['kode_negara']
namaNegara = ""
regionNegara = ""
subregionNegara = ""
                                                
for i in range(len(dfJ_2)):
    if list(dfJ_2['alpha-3'])[i]==kode_negara:
        namaNegara = list(dfJ_2['name'])[i]
        regionNegara = list(dfJ_2['region'])[i]
        subregionNegara = list(dfJ_2['sub-region'])[i]


c4.write('Negara dengan Produksi Terkecil Pada Keseluruhan Tahun')
col4.write(jumlahProduksi)
col4.write(kode_negara)
col4.write(namaNegara)
col4.write(regionNegara)
col4.write(subregionNegara)
 

#d bagian 3
dfproduksi0 = dfb[dfb.produksi == 0]
listnegara0 = []
listregio0 = []
listsubregio0 = []

for i in range(len(dfproduksi0)):
    for j in range(len(dfJ_2)):
        if list (dfproduksi0['kode_negara'])[i] == list(dfJ_2['alpha-3'])[j]:
            listnegara0.append(list(dfJ_2['name'])[j])
            listregio0.append(list(dfJ_2['region'])[j])
            listsubregio0.append(list(dfJ_2['sub-region'])[j])

dfproduksi0['negara'] = listnegara0
dfproduksi0['region'] = listregio0
dfproduksi0['sub-region'] = listsubregio0
 
                                                        
dfproduksikumulatif0 = dfb[dfb.produksi == 0]
listnegarakumulatif0 = []
listregionkumulatif0 = []
listsubregionkumulatif0 = []

for i in range(len(dfproduksikumulatif0)):
    for j in range(len(dfJ_2)):
        if list (dfproduksikumulatif0['kode_negara'])[i] == list(dfJ_2['alpha-3'])[j]:
            listnegarakumulatif0.append(list(dfJ_2['name'])[j])
            listregionkumulatif0.append(list(dfJ_2['region'])[j])
            listsubregionkumulatif0.append(list(dfJ_2['sub-region'])[j])

dfproduksikumulatif0['negara'] = listnegarakumulatif0
dfproduksikumulatif0['region'] = listregionkumulatif0
dfproduksikumulatif0['sub-region'] = listsubregionkumulatif0   

st.write('Data Negara dengan Produksi 0')                                                     
st.write(dfproduksi0)
st.write('Data Negara dengan Produksi Kumulatif 0')       
st.write(dfproduksikumulatif0)
