import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data_url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
gapminder = pd.read_csv(data_url)

ax = sns.boxplot(x='day',y='tip',data=gapminder)

plt.show()