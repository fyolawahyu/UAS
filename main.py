#IMPORT AWAL
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm 
import streamlit as st
from f_handler import csv_,json_

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

#MEMBUAT DATA FRAME TIAP FILE
st.title('Data Produksi Minyak Mentah')
st.header('UAS Pemrograman Komputer')
ch_ = csv_('produksi_minyak_mentah.csv')
jh_ = json_('kode_negara_lengkap.json')
csv_ = ch_.dataFrame
df_info = jh_.dataFrame
negara_li = df_info['name'].tolist()

list_kodekumpulannegara = []
for i in list(csv_['kode_negara']) :
    if i not in list(df_info['alpha-3']) :
        list_kodekumpulannegara.append(i)

for i in list_kodekumpulannegara :
    csv_ = csv_[csv_.kode_negara != i]
print(csv_)

#MENGATUR LETAK OUTPUT
st.sidebar.title("Pengaturan")
st.sidebar.header('Pengaturan Jumlah Produksi Per Bulan')
left_col, mid_col, right_col = st.columns(3)

#--a--
negara = st.sidebar.selectbox('Pilih negara : ',negara_li) 

kode = df_info[df_info['name']==negara]['alpha-3'].tolist()[0]

st.sidebar.write('Kode negara : ',kode)
st.sidebar.write('Negara : ',negara)

# MENGUBAH STRING MENJADI FLOAT
df['produksi'] = df['produksi'].astype(str).str.replace(".", "", regex=True).astype(float)
df['produksi'] = df['produksi'].astype(str).str.replace(",", "", regex=True).astype(float)
df['produksi'] = pd.to_numeric(df['produksi'], errors='coerce')

#OUTPUT TABEL A
df2 = pd.DataFrame(df,columns= ['kode_negara','tahun','produksi'])
df2=df2.loc[df2['kode_negara']==kode]
df2['produksi'] = pd.to_numeric(df2['produksi'], errors='coerce')

mid_col.write(df2)

#OUTPUT GRAFIK A
fig, ax = plt.subplots()
ax.plot(df2['tahun'], df2['produksi'], label = df2['tahun'], color='orange')
ax.set_title("Jumlah Produksi Per Tahun di Negara Pilihan")
ax.set_xlabel("Tahun", fontsize = 12)
ax.set_ylabel("Jumlah Produksi", fontsize = 12)
ax.legend(fontsize = 2)
plt.show()
st.pyplot(fig)

#--b--
st.write('Grafik Negara dengan Produksi Terbesar')
st.sidebar.header('Pengaturan Negara dengan Data Produksi Terbesar')
tahun = st.sidebar.number_input("Pilih Tahun produksi", min_value=1971, max_value=2015)
n = st.sidebar.number_input("Pilih Banyak Negara", min_value=1, max_value=None)

dfb = csv_.loc[csv_['tahun'] == tahun]
dfb = dfb.sort_values(by='produksi', ascending = False)
dfbaru = dfb[:n]

dfbaru.plot.bar(x='kode_negara', y='produksi')
plt.show()
st.pyplot(plt)

#--c--
st.write('Grafik Negara dengan Produksi Kumulatif Terbesar')
list_a = []
kumulatif = []

for i in list (csv_['kode_negara']) :
    if i not in list_a:
        list_a.append(i)
        
for i in list_a :
    a=csv_.loc[csv_['kode_negara'] ==i,'produksi'].sum()
    kumulatif.append(a)
    
dk = pd.DataFrame(list(zip(list_a,kumulatif)), columns = ['kode_negara','kumulatif'])
dk = dk.sort_values(by=['kumulatif'], ascending = False)
dk2 = dk.sort_values(by=['kumulatif'], ascending = True)
dk1 = dk[:n]

st.write(dk1)
dk1.plot.bar(x='kode_negara', y='kumulatif') 
plt.show()
st.pyplot(plt)

#--d--
col1, col2, col3, col4 = st.columns(4)
#bagian 1
jumlah_produksi = dfb[:1].iloc[0]['produksi']
kode_negara = dfb[:1].iloc[0]['kode_negara']
nama_negara = ""
region_negara = ""
subregion_negara = ""

for i in range(len(df_info)):
    if list(df_info['alpha-3'])[i]==kode_negara:
        nama_negara = list(df_info['name'])[i]
        region_negara = list(df_info['region'])[i]
        subregion_negara = list(df_info['sub-region'])[i]
        
col1.write('Negara dengan Produksi Terbesar')
col1.write(jumlah_produksi)
col1.write(kode_negara)
col1.write(nama_negara)
col1.write(region_negara)
col1.write(subregion_negara)

jumlah_produksi = dk[:1].iloc[0]['kumulatif']
kode_negara = dk[:1].iloc[0]['kode_negara']
nama_negara = ""
region_negara = ""
subregion_negara = ""

for i in range(len(df_info)):
    if list(df_info['alpha-3'])[i]==kode_negara:
        nama_negara = list(df_info['name'])[i]
        region_negara = list(df_info['region'])[i]
        subregion_negara = list(df_info['sub-region'])[i]
        
col2.write('Negara dengan Produksi Terbesar pada Keseluruhan Tahun')
col2.write(jumlah_produksi)
col2.write(kode_negara)
col2.write(nama_negara)
col2.write(region_negara)
col2.write(subregion_negara)


#bagian 2
dfterkecil = dfb[dfb.produksi !=0]
dfterkecil = dfterkecil.sort_values(by=['produksi'],ascending=True)
jumlah_produksi = dfterkecil[:1].iloc[0]['produksi']
kode_negara = dfterkecil[:1].iloc[0]['kode_negara']
nama_negara = ""
region_negara = ""
subregion_negara = ""
                                    
for i in range(len(df_info)):
    if list(df_info['alpha-3'])[i]==kode_negara:
        nama_negara = list(df_info['name'])[i]
        region_negara = list(df_info['region'])[i]
        subregion_negara = list(df_info['sub-region'])[i]
                                    
col3.write('Negara dengan Produksi Terkecil')
col3.write(jumlah_produksi)
col3.write(kode_negara)
col3.write(nama_negara)
col3.write(region_negara)
col3.write(subregion_negara)

dfakumulatifmin=dk2[dk2.kumulatif !=0]
dfakumulatifmin = dfakumulatifmin[:1].sort_values(by=['kumulatif'], ascending = True)
jumlah_produksi = dfakumulatifmin[:1].iloc[0]['kumulatif']
kode_negara = dfakumulatifmin[:1].iloc[0]['kode_negara']
nama_negara = ""
region_negara = ""
subregion_negara = ""
                                                
for i in range(len(df_info)):
    if list(df_info['alpha-3'])[i]==kode_negara:
        nama_negara = list(df_info['name'])[i]
        region_negara = list(df_info['region'])[i]
        subregion_negara = list(df_info['sub-region'])[i]


col4.write('Negara dengan Produksi Terkecil Pada Keseluruhan Tahun')
col4.write(jumlah_produksi)
col4.write(kode_negara)
col4.write(nama_negara)
col4.write(region_negara)
col4.write(subregion_negara)
 

#d bagian 3
dfproduksinol = dfb[dfb.produksi == 0]
listnegaranol = []
listregionol = []
listsubregionol = []

for i in range(len(dfproduksinol)):
    for j in range(len(df_info)):
        if list (dfproduksinol['kode_negara'])[i] == list(df_info['alpha-3'])[j]:
            listnegaranol.append(list(df_info['name'])[j])
            listregionol.append(list(df_info['region'])[j])
            listsubregionol.append(list(df_info['sub-region'])[j])

dfproduksinol['negara'] = listnegaranol
dfproduksinol['region'] = listregionol
dfproduksinol['sub-region'] = listsubregionol
 
                                                        
dfproduksikumulatifnol = dfb[dfb.produksi == 0]
listnegarakumulatifnol = []
listregionkumulatifnol = []
listsubregionkumulatifnol = []

for i in range(len(dfproduksikumulatifnol)):
    for j in range(len(df_info)):
        if list (dfproduksikumulatifnol['kode_negara'])[i] == list(df_info['alpha-3'])[j]:
            listnegarakumulatifnol.append(list(df_info['name'])[j])
            listregionkumulatifnol.append(list(df_info['region'])[j])
            listsubregionkumulatifnol.append(list(df_info['sub-region'])[j])

dfproduksikumulatifnol['negara'] = listnegarakumulatifnol
dfproduksikumulatifnol['region'] = listregionkumulatifnol
dfproduksikumulatifnol['sub-region'] = listsubregionkumulatifnol   

col_1, col_2= st.columns(2)                                                        
st.write(dfproduksinol)
st.write(dfproduksikumulatifnol)

