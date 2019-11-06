import pandas as pd

pew_df = pd.read_csv('data/pew.csv')

# 'religion', '<$10k', '$10-20k', '$20-30k', '$30-40k', '$40-50k', '$50-75k', '$75-100k', '$100-150k', '>150k', 'Don't know/refused'
print("the columns in the dataset", pew_df.columns)