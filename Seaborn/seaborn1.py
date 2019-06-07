import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset("titanic")

sns.pointplot(x = "sex", y = "survived", hue = "class", data = titanic)

plt.show()
