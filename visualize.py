import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'T:\task 1\dataset.csv.txt')
sns.set(style="whitegrid")

# Bar chart for gender distribution
sns.countplot(data=df, x='Gender', palette='pastel')
plt.title('Gender Distribution')
plt.savefig('gender_distribution.png')
plt.show()
sns.histplot(df['Age'], bins=5, kde=True, color='skyblue')
plt.title('Age Distribution')
plt.savefig('age_distribution.png')
plt.show()