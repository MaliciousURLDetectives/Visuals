import socket
import os
import pandas as pd
from bs4 import BeautifulSoup
import requests

os.chdir('C:\\Users\\georg\\OneDrive\\Desktop\\Complete Project\\Data Visualizations')
df=pd.read_csv('cybersecurity_attacks.csv')
source=df['Source IP Address']
x=[]

for i in range(100):
    x.append(source['Source IP Address'][i])

data=[]

for i in range(len(x)):
    data.append(requests.get("https://api.ip2location.io?key=EE8E963B2AD39180CD89C0F13946E917&ip="+x[i]+"&format=json").text)

df=pd.DataFrame(data,columns=['JSON Data'])
df.to_csv('Information2.csv')