import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("covid.csv")
print(data)
print(data.head())
# to get the list of all the columns
print(data.columns)
# end of the dataset
print(data.tail())
# statistics
print(data.describe())
data.isnull().sum()
#relating the variables with scatterplot
sns.relplot(x='Recovered', y='New deaths', hue='WHO Region',data=data)
#pairplot-combines both histogram and scatter plots,comprehensive snapshot of potential relationships within the data.
sns.pairplot(data)
sns.relplot(x='Recovered', y='New deaths', kind='line',data=data)
#Categorical scatter plot- is used when there are categorical variables
sns.catplot(x="WHO Region", y="Deaths", data=data)
plt.show()
#Mean number of deaths, total deaths especially to region, recovered,
# ratio of recovery to death and recovery to number of cases. in total, interventions trying to flatten curve
