import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("gapminderFiveYearData.csv")

ax = sns.boxplot(x='continent', y='lifeExp', data=data)

plt.show()