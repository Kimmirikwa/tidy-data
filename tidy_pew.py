import pandas as pd

# properties of tidy data
# 1. Each variable forms a column.
# 2. Each observation forms a row.
# 3. Each type of observational unit forms a table.

# pew dataset has one of the common issues of untidy data i.e it has column headers representing values instead of variables

pew_df = pd.read_csv('data/pew.csv')

# 'religion', '<$10k', '$10-20k', '$20-30k', '$30-40k', '$40-50k', '$50-75k', '$75-100k', '$100-150k', '>150k', 'Don't know/refused'
print("The columns in the unmolten dataset", pew_df.columns)

# from the columns above, we only have 3 variables i.e religion, income and frequency.  We need to convert this dataset
# to have only these variables as columns. only 'religion' is a variable in this dataframe. We are going to melt this dataframe. 
# 'religion' column will remain while the rest of the columns will be converted to 2 columns i.e 'income' and 'frequency'

molten_pew_df = pd.melt(pew_df, id_vars=['religion'], var_name='income', value_name='frequency')

print("The columns of the molten dataset", molten_pew_df.columns)

# creating a new file for this melted data
molten_pew_df.to_csv('results/molten_pew.csv', index=False)

