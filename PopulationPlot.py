#Amaris Efthimiou
#amaris.efthimiou66@myhunter.cuny.edu
#october 21, 2019
#Borough stats

import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv',skiprows=5)

b = input('Enter a borough:')

print('Minimum Population:', pop[b].min())
print('Average Population:', pop[b].mean())
print('Maximum Population:', pop[b].max())
