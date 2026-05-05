import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

print("Iris loaded!")
print(df)

# Q1: Print the shape of the dataset (rows, columns)
print(df.shape)

# Q2: Count how many flowers of each species
print(df["species"].value_counts())

# Q3: Calculate average sepal_length, sepal_width, petal_length, petal_width for each species
print(df.groupby('species').mean().round(1))

# Q4: Find which species has the largest petal_length (use idxmax)
largest=df.loc[df['petal_length'].idxmax()]
print(largest)

# Q5: Create a bar chart showing average petal_length by species
plt.figure(figsize=(8,6))
df.groupby('species')['petal_length'].mean().plot(kind='bar',color=['#FF6B6B','#4ECDC4','#45B7D1'])
plt.title('Average Petal Length By Species')
plt.ylabel('Length(cm)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('Petal_Length .png')
plt.show()

# Q6: Bar chart - Sepal length by species
plt.figure(figsize=(8,5))
df.groupby('species')['sepal_length'].mean().plot(kind='bar', color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
plt.title('Average Sepal Length by Species')
plt.ylabel('Length (cm)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('sepal_length.png')
plt.show()

# Q7: Create a scatter plot of sepal_length (x-axis) vs petal_length (y-axis)
# Color each species differently (setosa=red, versicolor=green, virginica=blue)
plt.figure(figsize=(8,5))
colors={'setosa':'red', 'versicolor':'green', 'virginica':'blue'}
for species, color in colors.items():
    subset=df[df['species']==species]
    plt.scatter(subset['sepal_length'],subset['petal_length'],c=color, label=species,alpha=0.7)
plt.title('Sepal Length VS Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.tight_layout()
plt.savefig('Scatter.png')
plt.show()

#Q8:Group by species and calculate mean
avg_measurements = df.groupby('species')[['sepal_length', 'petal_length']].mean()

#Q9:Create area chart
avg_measurements.plot(kind='area', alpha=0.6, color=['#66b3b2', '#ff9999'])

plt.title('Area Chart: Average Sepal Length vs Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Length (cm)')
plt.xticks(rotation=0)
plt.legend(labels=['Sepal Length', 'Petal Length'])
plt.tight_layout()
plt.savefig('area_chart.png')
plt.show()

#INSIGHTS
print("="*40)
print("WHAT I LEARNED FROM IRIS DATA")
print("="*40)

print("""
1. Setosa flowers have very small petals (1.5 cm)
2. Virginica flowers have big petals (5.5 cm)  
3. Versicolor flowers are in middle (4.3 cm)
4. Setosa is easy to separate from others
5. Petal length is best to find which flower is which
""")