import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset("iris")

ax = sns.violinplot(x='species',y='sepal_length',data=data)

plt.show()