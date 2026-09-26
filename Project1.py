import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Penguins Data.csv')

sns.scatterplot(data=df,x='flipper_length_mm',y='body_mass_g',hue='species')
plt.title('Flipper Length vs Body Mass by Species')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (grams)')
plt.show()

sns.pairplot(data=df,x='bill_length_mm',y='bill_depth_mm',hue='species')
sns.title('Bill Length vs Bill Depth by Species')
sns.xlabel('Bill Length (mm)')
sns.ylabel('Bill Depth (mm)')
plt.show()

sns.areaplot(data=df,x='bill_length_mm',y='bill_Mass_kg',hue='species')
sns.title('Bill Length vs Bill Mass by Species')
sns.xlabel('Bill Length (mm)')
sns.ylabel('Bill Mass (kg)')
plt.show()