#IMPORT AWAL
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm 
import streamlit as st
from f_handler import csv_,json_

#READ DATA JSON DAN MEMBUAT DATA FRAME JSON
with open("kode_negara_lengkap.json", "r") as readFile:
    data_json = json.load(readFile)
# for i in data:
#     print(type(i))
print(data_json[0])
dframe_json = pd.DataFrame(data_json)

#READ DATA CSV DAN MEMBUAT DATA FRAME CSV 1
data_csv = pd.read_csv("produksi_minyak_mentah.csv")
df_csv1 = pd.DataFrame(data_csv)

#TAMPILAN JUDUL DAN HEADER
st.title('Data Produksi Minyak Mentah')
st.header('UAS Pemrograman Komputer')
lst2_negara = dframe_json['name'].tolist()

#MENGHILANGKAN DATA SELAIN NEGARA
lst_negara = []
for i in list(df_csv1['kode_negara']) :
    if i not in list(dframe_json['alpha-3']) :
        lst_negara.append(i)

for i in lst_negara :
    df_csv1 = df_csv1[df_csv1.kode_negara != i]
print(df_csv1)

#MEMBUAT OUTPUT PENGATURAN
st.sidebar.title("Pengaturan")
st.sidebar.header('Pengaturan Jumlah Produksi Per Bulan')
left_col, mid_col, right_col = st.columns(3)

#---------------------------------------------------A------------------------------------------------------------

#MEMBUAT SELECTBOX UNTUK INPUTAN USER
negara = st.sidebar.selectbox('Pilih negara : ',lst2_negara) 
kode = dframe_json[dframe_json['name']==negara]['alpha-3'].tolist()[0]

st.sidebar.write('Negara : ',negara)
st.sidebar.write('Kode negara : ',kode)

# MENGUBAH STRING MENJADI FLOAT
df_csv1['produksi'] = df_csv1['produksi'].astype(str).str.replace(".", "", regex=True).astype(float)
df_csv1['produksi'] = df_csv1['produksi'].astype(str).str.replace(",", "", regex=True).astype(float)
df_csv1['produksi'] = pd.to_numeric(df_csv1['produksi'], errors='coerce')

#OUTPUT TABEL A
df2 = pd.DataFrame(df_csv1,columns= ['kode_negara','tahun','produksi'])
df2=df2.loc[df2['kode_negara']==kode]
df2['produksi'] = pd.to_numeric(df2['produksi'], errors='coerce')

mid_col.write(df2)

#OUTPUT GRAFIK A
fig, ax = plt.subplots()
ax.plot(df2['tahun'], df2['produksi'], label = df2['tahun'], color='orange')
ax.set_title("Jumlah Produksi Per Tahun di Negara Pilihan")
ax.set_xlabel("Tahun", fontsize = 12)
ax.set_ylabel("Jumlah Produksi", fontsize = 12)
plt.show()
st.pyplot(fig)

#---------------------------------------------------B------------------------------------------------------------

#MEMBUAT SELECTBOX UNTUK INPUTAN USER
st.write('Grafik Negara dengan Produksi Terbesar')
st.sidebar.header('Pengaturan Negara dengan Data Produksi Terbesar')
tahun = st.sidebar.number_input("Pilih Tahun produksi", min_value=1971, max_value=2015)
n = st.sidebar.number_input("Pilih Banyak Negara", min_value=1, max_value=None)

#MEMBUAT DATA FRAME NEGARA PRODUKSI TERBANYAK PER TAHUN
dfb = df_csv1.loc[df_csv1['tahun'] == tahun]
dfb = dfb.sort_values(by='produksi', ascending = False)
dfbaru = dfb[:n]

#PLOTTING NEGARA PRODUKSI TERBANYAK PER TAHUN
dfbaru.plot.bar(x='kode_negara', y='produksi')
plt.show()
st.pyplot(plt)

#---------------------------------------------------B------------------------------------------------------------
st.write('Grafik Negara dengan Produksi Kumulatif Terbesar')
list_a = []
kumulatif = []

for i in list (df_csv1['kode_negara']) :
    if i not in list_a:
        list_a.append(i)
        
for i in list_a :
    a=df_csv1.loc[df_csv1['kode_negara'] ==i,'produksi'].sum()
    kumulatif.append(a)
    
dk = pd.DataFrame(list(zip(list_a,kumulatif)), columns = ['kode_negara','kumulatif'])
dk = dk.sort_values(by=['kumulatif'], ascending = False)
dk = dk[:n]

dk.plot.bar(x='kode_negara', y='kumulatif') 
plt.show()
st.pyplot(plt)

#--d--
#bagian 1
jumlah_produksi = dfb[:1].iloc[0]['produksi']
kode_negara = dfb[:1].iloc[0]['kode_negara']
nama_negara = ""
region_negara = ""
subregion_negara = ""

for i in range(len(dframe_json)):
    if list(dframe_json['alpha-3'])[i]==kode_negara:
        nama_negara = list(dframe_json['name'])[i]
        region_negara = list(dframe_json['region'])[i]
        subregion_negara = list(dframe_json['sub-region'])[i]
        
left_col.write('Negara dengan Produksi Terbesar')
left_col.write(jumlah_produksi)
left_col.write(kode_negara)
left_col.write(nama_negara)
left_col.write(region_negara)
left_col.write(subregion_negara)

jumlah_produksi = dk[:1].iloc[0]['kumulatif']
kode_negara = dk[:1].iloc[0]['kode_negara']
nama_negara = ""
region_negara = ""
subregion_negara = ""

for i in range(len(dframe_json)):
    if list(dframe_json['alpha-3'])[i]==kode_negara:
        nama_negara = list(dframe_json['name'])[i]
        region_negara = list(dframe_json['region'])[i]
        subregion_negara = list(dframe_json['sub-region'])[i]
        
left_col.write('Negara dengan Produksi Terbesar pada Keseluruhan Tahun')
left_col.write(jumlah_produksi)
left_col.write(kode_negara)
left_col.write(nama_negara)
left_col.write(region_negara)
left_col.write(subregion_negara)


#bagian 2
dfterkecil = dfb[dfb.produksi !=0]
dfterkecil = dfterkecil.sort_values(by=['produksi'],ascending=True)
jumlah_produksi = dfterkecil[:1].iloc[0]['produksi']
kode_negara = dfterkecil[:1].iloc[0]['kode_negara']
nama_negara = ""
region_negara = ""
subregion_negara = ""
                                    
for i in range(len(dframe_json)):
    if list(dframe_json['alpha-3'])[i]==kode_negara:
        nama_negara = list(dframe_json['name'])[i]
        region_negara = list(dframe_json['region'])[i]
        subregion_negara = list(dframe_json['sub-region'])[i]
                                    
st.write('Negara dengan Produksi Terkecil')
st.write(jumlah_produksi)
st.write(kode_negara)
st.write(nama_negara)
st.write(region_negara)
st.write(subregion_negara)
                                    
dfakumulatifmin=dk[dk.kumulatif !=0]
dfakumulatifmin = dfakumulatifmin[:1].sort_values(by=['kumulatif'], ascending = True)
jumlah_produksi = dfakumulatifmin[:1].iloc[0]['kumulatif']
kode_negara = dfakumulatifmin[:1].iloc[0]['kode_negara']
nama_negara = ""
region_negara = ""
subregion_negara = ""
                                                
for i in range(len(dframe_json)):
    if list(dframe_json['alpha-3'])[i]==kode_negara:
        nama_negara = list(dframe_json['name'])[i]
        region_negara = list(dframe_json['region'])[i]
        subregion_negara = list(dframe_json['sub-region'])[i]
                                                
st.write('Negara dengan Produksi Terkecil Pada Keseluruhan Tahun')
st.write(jumlah_produksi)
st.write(kode_negara)
st.write(nama_negara)
st.write(region_negara)
st.write(subregion_negara)

#d bagian 3
dfproduksinol = dfb[dfb.produksi == 0]
listnegaranol = []
listregionol = []
listsubregionol = []

for i in range(len(dfproduksinol)):
    for j in range(len(dframe_json)):
        if list (dfproduksinol['kode_negara'])[i] == list(dframe_json['alpha-3'])[j]:
            listnegaranol.append(list(dframe_json['name'])[j])
            listregionol.append(list(dframe_json['region'])[j])
            listsubregionol.append(list(dframe_json['sub-region'])[j])

dfproduksinol['negara'] = listnegaranol
dfproduksinol['region'] = listregionol
dfproduksinol['sub-region'] = listsubregionol
 
                                                        
dfproduksikumulatifnol = dfb[dfb.produksi == 0]
listnegarakumulatifnol = []
listregionkumulatifnol = []
listsubregionkumulatifnol = []

for i in range(len(dfproduksikumulatifnol)):
    for j in range(len(dframe_json)):
        if list (dfproduksikumulatifnol['kode_negara'])[i] == list(dframe_json['alpha-3'])[j]:
            listnegarakumulatifnol.append(list(dframe_json['name'])[j])
            listregionkumulatifnol.append(list(dframe_json['region'])[j])
            listsubregionkumulatifnol.append(list(dframe_json['sub-region'])[j])

dfproduksikumulatifnol['negara'] = listnegarakumulatifnol
dfproduksikumulatifnol['region'] = listregionkumulatifnol
dfproduksikumulatifnol['sub-region'] = listsubregionkumulatifnol     
                                                        
st.write(dfproduksinol)
st.write(dfproduksikumulatifnol)

