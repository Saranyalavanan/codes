import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("datasets/weatherdata.csv")
print(data.head())

data['time'] = pd.to_datetime(data['time'])  

plt.plot(data["time"],data["temperature"],color="orange")
plt.show()

plt.plot(data["time"],data["relative_humidity"],color="skyblue")
plt.show()

plt.plot(data["time"],data["dew_point"],color="grey")
plt.show() 
