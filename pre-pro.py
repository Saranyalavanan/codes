import pandas as pd
from sklearn.preprocessing import *

data=pd.read_csv("market.csv",encoding='ISO-8859-1') 

data["Order Date"]=pd.to_datetime(data["Order Date"])
print(data["Order Date"])

cat=["Customer Name","Product Category","Region","Province","Product Sub-Category","Product Container","Ship Mode","Order Priority"]
label_encode=LabelEncoder()
for  c in cat:
    data[c]=label_encode.fit_transform(data[c])
    print(data[c])

num=["Order Quantity","Sales","Discount","Profit","Unit Price","Shipping Cost","Product Base Margin"]
scaler=MinMaxScaler()
data[num]=scaler.fit_transform(data[num])
print(data[num])
