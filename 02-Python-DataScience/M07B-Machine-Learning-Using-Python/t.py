import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the Iris dataset
# iris = sns.load_dataset('iris.csv')
iris = sns.load_dataset('iris')

# Display the first few rows
print(iris.head())

# Pairplot to visualize the relationships between variables
sns.pairplot(iris, hue='species')
plt.show()

