Data Visualization - Gender and Age Distribution
📌 Overview
This project demonstrates how to visualize the distribution of categorical and continuous variables using Python.
We use a dataset containing demographic information to create:

Bar chart for gender distribution (categorical variable)

Histogram for age distribution (continuous variable)

Both visualizations are saved as PNG files for further use or reporting.

📂 Files in This Project
dataset.csv.txt → The dataset used for visualization.

visualization.py → Python script containing the code to generate the charts.

gender_distribution.png → Bar chart showing the distribution of genders.

age_distribution.png → Histogram showing the distribution of ages.

📜 Requirements
To run this project, make sure you have Python 3.x installed along with the following libraries:

bash
Copy
Edit
pip install pandas seaborn matplotlib

🖥️ How to Run
Clone this repository:

bash
Copy
Edit
git clone https://github.com/tanmayy06/PRODIGY_DS_01/tree/main
Navigate to the project folder:

bash
Copy
Edit
cd <your-repo-name>
Place your dataset in the folder (already included as dataset.csv.txt).

Run the script:

bash
Copy
Edit
python visualization.py

📊 Code Explanation
python
Copy
Edit
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r'T:\task 1\dataset.csv.txt')

# Set Seaborn style
sns.set(style="whitegrid")

# Bar chart for categorical variable (Gender)
sns.countplot(data=df, x='Gender', palette='pastel')
plt.title('Gender Distribution')
plt.savefig('gender_distribution.png')
plt.show()

# Histogram for continuous variable (Age)
sns.histplot(df['Age'], bins=5, kde=True, color='skyblue')
plt.title('Age Distribution')
plt.savefig('age_distribution.png')
plt.show()

📈 Output Examples
Gender Distribution: Shows how many individuals belong to each gender category.

Age Distribution: Shows how ages are spread across the dataset, including a kernel density estimate (KDE) line for smoother interpretation.

✨ Author
Tanmay Gupta
Data Science Intern
