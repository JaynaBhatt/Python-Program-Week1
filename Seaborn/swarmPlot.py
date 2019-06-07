import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("tips.csv")

ax = sns.swarmplot(x='total_bill',y='size',data=data)

plt.show()