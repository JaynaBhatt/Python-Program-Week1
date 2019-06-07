import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset("tips")

ax = sns.violinplot(x='sex',y='total_bill',data=data)
plt.show()
