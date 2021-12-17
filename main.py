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
dfC_2 = pd.DataFrame(dfC_1,columns= ['kode_negara','tahun','produksi'])
dfC_2=dfC_2.loc[dfC_2['kode_negara']==kode]
dfC_2['produksi'] = pd.to_numeric(dfC_2['produksi'], errors='coerce')

left_col.write(dfC_2)

#OUTPUT GRAFIK A
fig, ax = plt.subplots()
ax.plot(dfC_2['tahun'], dfC_2['produksi'], label = dfC_2['tahun'], color='orange')
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

dfB = dfC_2.loc[dfC_2['tahun'] == tahun]
dfB = dfB.sort_values(by='produksi', ascending = False)
dfB_2 = dfB[:n]
lcol.write(dfB_2)
'''
dfB_2.plot.bar(x='kode_negara', y='produksi')
plt.show()
rcol.pyplot(plt)
'''
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
jumlahProd = dfB[:1].iloc[0]['produksi']
kodeNegara = dfB[:1].iloc[0]['kode_negara']
namaNegara = ""
regionNegara = ""
subregionNegara = ""

for i in range(len(dfJ_2)):
    if list(dfJ_2['alpha-3'])[i]==kode_negara:
        namaNegara = list(dfJ_2['name'])[i]
        regionNegara = list(dfJ_2['region'])[i]
        subregionNegara = list(dfJ_2['sub-region'])[i]
        
c1.write('Negara dengan Produksi Terbesar')
col1.write(jumlahProd)
col1.write(kodeNegara)
col1.write(namaNegara)
col1.write(regionNegara)
col1.write(subregionNegara)

jumlahProd = dk[:1].iloc[0]['kumulatif']
kodeNegara = dk[:1].iloc[0]['kode_negara']
namaNegara = ""
regionNegara = ""
subregionNegara = ""

for i in range(len(dfJ_2)):
    if list(dfJ_2['alpha-3'])[i]==kode_negara:
        namaNegara = list(dfJ_2['name'])[i]
        regionNegara = list(dfJ_2['region'])[i]
        subregionNegara = list(dfJ_2['sub-region'])[i]
        
c2.write('Negara dengan Produksi Terbesar pada Keseluruhan Tahun')
col2.write(jumlahProd)
col2.write(kodeNegara)
col2.write(namaNegara)
col2.write(regionNegara)
col2.write(subregionNegara)


#bagian 2
dfD_kecil = dfB[dfB.produksi !=0]
dfD_kecil = dfD_kecil.sort_values(by=['produksi'],ascending=True)
jumlahProd = dfD_kecil[:1].iloc[0]['produksi']
kodeNegara = dfD_kecil[:1].iloc[0]['kode_negara']
namaNegara = ""
regionNegara = ""
subregionNegara = ""
                                    
for i in range(len(dfJ_2)):
    if list(dfJ_2['alpha-3'])[i]==kode_negara:
        namaNegara = list(dfJ_2['name'])[i]
        regionNegara = list(dfJ_2['region'])[i]
        subregionNegara = list(dfJ_2['sub-region'])[i]
                                    
c3.write('Negara dengan Produksi Terkecil')
col3.write(jumlahProd)
col3.write(kodeNegara)
col3.write(namaNegara)
col3.write(regionNegara)
col3.write(subregionNegara)

dfD_akumulatifkecil=dk2[dk2.kumulatif !=0]
dfD_akumulatifkecil = dfD_akumulatifkecil[:1].sort_values(by=['kumulatif'], ascending = True)
jumlahProd = dfD_akumulatifkecil[:1].iloc[0]['kumulatif']
kodeNegara = dfD_akumulatifkecil[:1].iloc[0]['kode_negara']
namaNegara = ""
regionNegara = ""
subregionNegara = ""
                                                
for i in range(len(dfJ_2)):
    if list(dfJ_2['alpha-3'])[i]==kode_negara:
        namaNegara = list(dfJ_2['name'])[i]
        regionNegara = list(dfJ_2['region'])[i]
        subregionNegara = list(dfJ_2['sub-region'])[i]


c4.write('Negara dengan Produksi Terkecil Pada Keseluruhan Tahun')
col4.write(jumlahProd)
col4.write(kodeNegara)
col4.write(namaNegara)
col4.write(regionNegara)
col4.write(subregionNegara)
 

#d bagian 3
dfD_produksi0 = dfB[dfB.produksi == 0]
lst_negara0 = []
lst_regional0 = []
lst_subregional0 = []

for i in range(len(dfD_produksi0)):
    for j in range(len(dfJ_2)):
        if list (dfD_produksi0['kode_negara'])[i] == list(dfJ_2['alpha-3'])[j]:
            lst_negara0.append(list(dfJ_2['name'])[j])
            lst_regional0.append(list(dfJ_2['region'])[j])
            lst_subregional0.append(list(dfJ_2['sub-region'])[j])

dfD_produksi0['negara'] = lst_negara0
dfD_produksi0['region'] = lst_regional0
dfD_produksi0['sub-region'] = lst_subregional0
 
                                                        
dfD_produksikumulatif0 = dfB[dfB.produksi == 0]
lst_negarakumulatif0 = []
lst_regionkumulatif0 = []
lst_subregionkumulatif0 = []

for i in range(len(dfD_produksikumulatif0)):
    for j in range(len(dfJ_2)):
        if list (dfD_produksikumulatif0['kode_negara'])[i] == list(dfJ_2['alpha-3'])[j]:
            lst_negarakumulatif0.append(list(dfJ_2['name'])[j])
            lst_regionkumulatif0.append(list(dfJ_2['region'])[j])
            lst_subregionkumulatif0.append(list(dfJ_2['sub-region'])[j])

dfD_produksikumulatif0['negara'] = lst_negarakumulatif0
dfD_produksikumulatif0['region'] = lst_regionkumulatif0
dfD_produksikumulatif0['sub-region'] = lst_subregionkumulatif0   

st.write('Data Negara dengan Produksi Nol')                                                     
st.write(dfD_produksi0)
st.write('Data Negara dengan Produksi Kumulatif Nol')       
st.write(dfD_produksikumulatif0)
