import streamlit as st
import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt
from matplotlib import cm, colors

##### Tittle
st.set_page_config(layout="wide")  # this needs to be the first Streamlit command called
st.title("Statistik Produksi Minyak Mentah Berbagai Negara")
st.markdown("**")

##### Sidebar
st.sidebar.title("Pengaturan")
left_col, mid_col, right_col = st.columns(3)

##### Read Data CSV dan ubah ke data frame
csv = pd.read_csv("produksi_minyak_mentah.csv")
df = pd.DataFrame(csv)

##### Mengubah string menjadi float pada data produksi
#df['produksi'] = df['produksi'].astype(str).str.replace(".", "", regex=True).astype(float)
#df['produksi'] = df['produksi'].astype(str).str.replace(",", "", regex=True).astype(float)
#df['produksi'] = pd.to_numeric(df['produksi'], errors='coerce')

kode_csv = list(df['kode_negara'].unique())
#print(f"kode_negara: {kode_csv}")
total_produksi = []
for c in kode_csv:
    produksi = df[df['produksi']==c]['produksi'].astype(float)
    total_produksi.append(produksi.sum())
#print(f"Total produksi: {total_produksi}")

##### Read Data Json
with open ("kode_negara_lengkap.json") as f:
    file_json = json.load(f)
df2 = pd.DataFrame(file_json)

#kode_json = list(map(lambda kode_json: kode_json['alpha-3'], file_json))
kode_json = df2['alpha-3'].tolist()
#print(kode_json)

#nama_negara = list(map(lambda nama_negara: nama_negara['name'], file_json))
nama_negara = df2['name'].tolist()
#print(nama_negara)

##### User inputs on the control panel
st.sidebar.subheader("Pengaturan konfigurasi tampilan")
list_kode=[]
for k in kode_csv:
    if k not in kode_json:
        continue
    list_kode.append(k)
#print(list_kode)

list_negara=[]
for i in file_json:
    if i['alpha-3'] not in list_kode:
        continue
    list_negara.append(i['name'])
#print(list_negara)
negara = st.sidebar.selectbox("Pilih Negara", list_negara)
kode = df2[df2['name']==negara]['alpha-3'].tolist()[0]
n_tampil = st.sidebar.number_input("Jumlah baris dalam tabel yang ditampilkan", min_value=1, max_value=None, value=10)

list_tahun = list(df['tahun'].unique())
tahun = st.sidebar.selectbox("Pilih Tahun", list_tahun)


# A
left_col.subheader("Tabel representasi data")

dfA = pd.DataFrame(df, columns=['kode_negara', 'tahun', 'produksi'])
dfA = dfA.loc[dfA['kode_negara']==kode]
dfA['produksi'] = pd.to_numeric(dfA['produksi'], errors='coerce')

fig, ax = plt.subplots()
ax.plot(dfA['tahun'], dfA['produksi'], label = negara)
ax.set_title("Jumlah Produksi Per Tahun")
ax.set_xlabel("Tahun", fontsize = 9)
ax.set_ylabel("Jumlah Produksi", fontsize = 9)
ax.legend(fontsize = 9)
st.pyplot(fig)

left_col.dataframe(dfA.head(n_tampil))

'''#IMPORT AWAL
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

st.write(df2)

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
mid_col.write('Grafik Negara dengan Produksi Terbanyak')
st.sidebar.header('Pengaturan Negara dengan Data Produksi Terbesar')
tahun = st.sidebar.number_input("Pilih Tahun produksi", min_value=1971, max_value=2015)
n = st.sidebar.number_input("Pilih Banyak Negara", min_value=1, max_value=None)

dfb = df.loc[df['tahun'] == tahun][:n]
dfb = dfb.sort_values(by='produksi', ascending = False)
dfb = dfb[:n]

dfb.plot.bar(x='kode_negara', y='produksi')
plt.show()
st.pyplot(plt)

#--c--
mid_col.write('Grafik Negara dengan Data Produksi Kumulatif Terbanyak')
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

for i in range(len(df_info)):
    if list(df_info['alpha-3'])[i]==kode_negara:
        nama_negara = list(df_info['name'])[i]
        region_negara = list(df_info['region'])[i]
        subregion_negara = list(df_info['sub-region'])[i]
        
left_col.write('Negara dengan Produksi Terbesar pada Keseluruhan Tahun')
left_col.write(jumlah_produksi)
left_col.write(kode_negara)
left_col.write(nama_negara)
left_col.write(region_negara)
left_col.write(subregion_negara)


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
#d bagian 3
dfproduksinol = dfb[dfb.produksi == 0]
listnegaranol = []
listregionol = []
listsubregionol = []

for i in range(len(dfproduksinol)):
    for j in range(len(df_info)):
        if list (dfb['kode_negara'])[i] == list(df_info['alpha-3])[j]:
            listnegaranol.append(list(df_info['name'])[j])
            listregional.append(list(df_info['region'])[j])
            listsubregionol.append(list(df_info['sub-region'])[j])

dfproduksinol['negara'] = listnegaranol
dfproduksinol['region'] = listregional
dfproduksinol['sub-region'] = listsubregionol
 
                                                        
dfproduksinolkumulatifnol = dfb[dfb.produksi == 0]
listnegarakumulatifnol = []
listregionkumulatifnol = []
listsubregionkumulatifnol = []

for i in range(len(dfproduksikumulatifnol)):
    for j in range(len(df_info)):
        if list (dfb['kode_negara'])[i] == list(df_info['alpha-3])[j]:
            listnegarankumulatifnol.append(list(df_info['name'])[j])
            listregionalkumulatifnol.append(list(df_info['region'])[j])
            listsubregionkumulatifnol.append(list(df_info['sub-region'])[j])

dfproduksikumulatifnol['negara'] = listnegarankumulatifnol
dfproduksikumulatifnol['region'] = listregional
dfproduksikumulatifnol['sub-region'] = listsubregionkumulatifnol     
                                                        
st.write(dfproduksinol}
st.write(dfproduksinol}
