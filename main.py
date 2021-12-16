#IMPORT AWAL
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm 
import streamlit as st
from f_handler import csv_,json_

list_kodenegarahuruf = []
list_organisasi = []
list_nama = []
list_kodenegaraangka = []
list_region = []
list_subregion = []

st.title('Data Produksi Minyak Mentah')
st.header('UAS Pemrograman Komputer')
left_col, mid_col, right_col = st.columns(3)

#READ DATA JSON
with open("kode_negara_lengkap.json", "r") as read_file:
    data = json.load(read_file)
# for i in data:
#     print(type(i))
print(data[0])
df_json = pd.DataFrame(data)

#READ DATA CSV
csv = pd.read_csv("produksi_minyak_mentah.csv")
df_csv = pd.DataFrame(csv)

# Membuat list kode negara dari df_csv
for i in list(df_csv['kode_negara']):
    if i not in list_kodenegarahuruf:
        list_kodenegarahuruf.append(i)

# Mencari organisasi/kumpulan negara pada list_kodenegarahuruf
for i in list_kodenegarahuruf:
    if i not in list(df_json['alpha-3']):
        list_organisasi.append(i)
        
# Menghilangkan organisasi/kumpulan negara dari df_csv
for i in list_organisasi:
    df_csv = df_csv[df_csv.kode_negara != i]
    if i in list_kodenegarahuruf:
        list_kodenegarahuruf.remove(i)

# Membuat beberapa list yang berisi informasi tentang nama negara, kode
# negara angka, region, dan sub-region dari tiap negara pada df_csv
for i in range(len(list_kodenegarahuruf)):
    for j in range(len(list(df_json['alpha-3']))):
        if list(df_json['alpha-3'])[j] == list_kodenegarahuruf[i] and list(df_json['name'])[j] not in list_nama:
            list_nama.append(list(df_json['name'])[j])
            list_kodenegaraangka.append(list(df_json['country-code'])[j])
            list_region.append(list(df_json['region'])[j])
            list_subregion.append(list(df_json['sub-region'])[j])
            
# Membuat dataframe dari list yang berisi informasi tiap negara pada df_csv
df_negara = pd.DataFrame(list(zip(list_nama, list_kodenegarahuruf, list_kodenegaraangka, list_region, list_subregion)), columns=[
                         'Negara', 'alpha-3', 'Kode_Negara', 'Region', 'Sub-Region'])

N = st.sidebar.selectbox('Pilih negara : ',list_nama)
for i in range(len(list_nama)):
    if list_nama[i] == N:
        kodenegarahuruf = list_kodenegarahuruf[i]
        kodenegaraangka = list_kodenegaraangka[i]
        region = list_region[i]
        subregion = list_subregion[i]
        
# Membuat list baru untuk menampung data produksi negara dan tahunnya
list_produksi = []
list_tahun = []

# Mengambil data produksi dan tahun berdasarkan negara yang dipilih pada
# option dan memasukkannya ke list yang telah dibuat
for i in range(len(list(df_csv['kode_negara']))):
    if kodenegarahuruf == list(df_csv['kode_negara'])[i]:
        list_produksi.append(list(df_csv['produksi'])[i])
        list_tahun.append(list(df_csv['tahun'])[i])

#OUTPUT GRAFIK A
fig, ax = plt.subplots()
ax.plot(list_tahun, list_produksi)
ax.set_title("Jumlah Produksi Per Tahun di Negara Pilihan")
ax.set_xlabel("Tahun", fontsize = 12)
ax.set_ylabel("Jumlah Produksi", fontsize = 12)
ax.legend(fontsize = 2)
plt.show()
st.pyplot(fig)     

#--------------------------b-------------------------------
st.sidebar.footer('Pengaturan Negara dengan Produksi Terbesar')
tahun == t
tahun = st.sidebar.number_input("Pilih Tahun produksi", min_value=1971, max_value=2015)
n = st.sidebar.number_input("Pilih Banyak Negara", min_value=1, max_value=None)

dfb = df_scv.loc[df_scv['tahun'] == tahun [:n]
dfb = dfb.sort_values(by='produksi', ascending = False)
df3 = dfb[:n]

list_nama_df2 = []

# Memasukkan nama negara dari df_negara ke list_nama_df2 berdasarkan data
# dari df2
for i in range(len(list(dfb['kode_negara']))):
    for j in range(len(list(df_negara['alpha-3']))):
        if list(df2['kode_negara'])[i] == list(df_negara['alpha-3'])[j]:
            list_nama_df2.append(list(df_negara['Negara'])[j])

dfb['negara'] = list_nama_df2

dfb = df2[:n]

dfb.plot.bar(x='kode_negara', y='produksi')
plt.show()
st.pyplot(plt)

        
'''
#MEMBUAT DATA FRAME TIAP FILE

ch_ = csv_('produksi_minyak_mentah.csv')
jh_ = json_('kode_negara_lengkap.json')
csv_ = ch_.dataFrame
df_info = jh_.dataFrame
negara_li = df_info['name'].tolist()


#MENGATUR LETAK OUTPUT
st.sidebar.title("Pengaturan")
st.sidebar.header('Pengaturan Jumlah Produksi Per Bulan')
left_col, mid_col, right_col = st.columns(3)
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
ax.plot(df2['tahun'], df2['produksi'], label = df2['tahun'])
ax.set_title("Jumlah Produksi Per Tahun di Negara Pilihan")
ax.set_xlabel("Tahun", fontsize = 12)
ax.set_ylabel("Jumlah Produksi", fontsize = 12)
ax.legend(fontsize = 2)
plt.show()
st.pyplot(fig)

#--b--

st.sidebar.header('Pengaturan Negara dengan Produksi Terbesar')
tahun = st.sidebar.number_input("Pilih Tahun produksi", min_value=1971, max_value=2015)
n = st.sidebar.number_input("Pilih Banyak Negara", min_value=1, max_value=None)

dfb = df.loc[df['tahun'] == tahun][:n]
dfb = dfb.sort_values(by='produksi', ascending = False)
df3 = dfb[:n]

df3.plot.bar(x='kode_negara', y='produksi')
plt.show()
st.pyplot(plt)

#--c--
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

for i in range(len(df_info)):
    if list(df_info['alpha-3'])[i]==kode_negara:
        nama_negara = list(df_info['name'])[i]
        region_negara = list(df_info['region'])[i]
        subregion_negara = list(df_info['sub-region'])[i]

st.write('Negara dengan Produksi Terbesar')
st.write(jumlah_produksi)
st.write(kode_negara)
st.write(nama_negara)
st.write(region_negara)
st.write(subregion_negara)

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

st.write('Negara dengan Produksi Terbesar pada Keseluruhan Tahun')
st.write(jumlah_produksi)
st.write(kode_negara)
st.write(nama_negara)
st.write(region_negara)
st.write(subregion_negara)


#bagian 2
dfterkecil = dfb[dfb.produksi !=0]
dfterkecil = dfterkecil.sort_values(by=['produksi'],ascending=True]

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

st.write('Negara dengan Produksi Terkecil')
st.write(jumlah_produksi)
st.write(kode_negara)
st.write(nama_negara)
st.write(region_negara)
st.write(subregion_negara)

dfkumulatifmin=dk[dk.kumulatif !=0]
dfkumulatifmin = dfkumulatifmin[:1].sort_values(by=['produksi'], ascending = True]

jumlah_produksi = dfkumulatifmin[:1].iloc[0]['kumulatif']
kode_negara = dfkumulatifmin[:1].iloc[0]['kode_negara']
nama_negara = ""
region_negara = ""
subregion_negara = ""

for i in range(len(df_info)):
    if list(df_info['alpha-3'])[i]==kode_negara:
        nama_negara = list(df_info['name'])[i]
        region_negara = list(df_info['region'])[i]
        subregion_negara = list(df_info['sub-region'])[i]

st.write('Negara dengan Produksi Terkecil Pada Keseluruhan Tahun')
st.write(jumlah_produksi)
st.write(kode_negara)
st.write(nama_negara)
st.write(region_negara)
st.write(subregion_negara)
'''
