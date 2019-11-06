import pandas as pd

billboard_df = pd.read_csv('data/billboard.csv')

# the columns of the data
print("The columns of the raw data", billboard_df.columns.tolist())

# we start by first melting the dataset
molten_billboard_df = pd.melt(billboard_df, 
	id_vars=['year', 'artist.inverted', 'track', 'time', 'genre', 'date.entered', 'date.peaked'], var_name='week')
print("the molten dataset columns", molten_billboard_df.columns.tolist())