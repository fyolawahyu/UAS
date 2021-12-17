import pandas as pd
import numpy as np
import json

class json_:
    def __init__(slf,f_name):
        slf.f_name = f_name
        with open(f_name, "r") as read_file:
            slf.data = json.load(read_file)
        dic = {}
        key_li = list(slf.data[0].keys())
        for key in key_li:
            dic[key] = []
        for i in slf.data:
            for key in key_li:
                dic[key].append(i[key])
        slf.dataFrame = pd.DataFrame(dic)
    def jsonToCsv(slf,f_csv):
        slf.dataFrame.to_csv('{}.csv'.format(f_csv),index=False) 
        
class csv_:
    def __init__(slf,f_name):
        slf.f_name = f_name
        df = pd.read_csv(f_name)
        slf.data = {}
        for i in df:
            slf.data[i]=df[i].tolist()
        slf.dataFrame = df
    def csvToJson(slf,f_json):
        df = pd.read_csv(slf.f_name)
        lst = []
        for i in range(len(df)):
            r = {}
            for j in df:
                try :
                    a = float(df[j][i])
                except:
                    a = str(df[j][i]) 
                r[j] = a
            lst.append(r)
        with open("{}.json".format(f_json), "w") as f_write:
            json.dump(lst,f_write)

