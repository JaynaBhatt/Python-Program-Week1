import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data_url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
data = pd.read_csv(data_url)

ax = sns.swarmplot(x='total_bill',y='day',data=data)

plt.show()