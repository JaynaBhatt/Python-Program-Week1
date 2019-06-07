import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.read_csv('medal.csv')

country_data = df["country"]
medal_data = df["gold_medal"]

colors = ['red','orange','blue','pink','green','yellow']

explode = (0.1,0,0,0,0)

plt.pie(medal_data,labels=country_data,explode=explode,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
plt.title('Data imported from CSV file')

plt.show()