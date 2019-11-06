import pandas as pd

pew_df = pd.read_csv('data/pew.csv')

# 'religion', '<$10k', '$10-20k', '$20-30k', '$30-40k', '$40-50k', '$50-75k', '$75-100k', '$100-150k', '>150k', 'Don't know/refused'
print("The columns in the unmolten dataset", pew_df.columns)

# from the columns above, we only have 3 variables i.e religion, income and frequency.  We need to convert this dataset
# to have only these variables as columns. We are going to melt this dataframe. 
# 'religion' column will remain while the rest of the columns will be converted to 2 columns i.e 'income' and 'frequency'

molten_pew_df = pd.melt(pew_df, id_vars=['religion'])

print("The columns of the molten dataset", molten_pew_df.columns)