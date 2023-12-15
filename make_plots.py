import pandas as pd
import plotly.offline as pyo
import plotly.express as px
'''
df=pd.read_csv('data.csv')
for i in range(len(df['Country_Code'])):
    if df['Malicious'][i]<1.02:
        df['Country_Code'][i]='Other'
fig = px.pie(df, names='Country_Code', values='Malicious', title='Malicious URLS by Countries')
pyo.plot(fig, filename='dashboard1.html')
'''

'''
df=pd.read_csv('cybersecurity_attacks.csv')
df=df['Attack Type']
count={}
for i in df:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
t=13307+13428+13265
c={'Types of Attacks':['Malware','DDoS','Intrusion'],
   'Percentages':[100*13307/t,100*13428/t,100*13265/t]}
df=pd.DataFrame(c)

fig = px.bar(c, x='Types of Attacks', y='Percentages', title='Types Of Malicious Attacks! '+str(t)+' Data Points Analyzed')
pyo.plot(fig, filename='dashboard2.html')

data={'Server':['Apache','nginx','Microsoft','Other'],'Percentage of Server':[.565,.306,.0704,.056]}

df=pd.DataFrame(data)

fig = px.bar(df, x='Percentage of Server', y='Server', orientation='h', title='1800 Servers Analyzed')

pyo.plot(fig, filename='index.html')
'''
