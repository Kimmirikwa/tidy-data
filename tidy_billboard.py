import pandas as pd
import re

def extract_week(row):
	week_no = re.findall(r'\d+', row['week'])[0]
	return week_no

billboard_df = pd.read_csv('data/billboard.csv')

# the columns of the data
print("The columns of the raw data", billboard_df.columns.tolist())

# we start by first melting the dataset
molten_billboard_df = pd.melt(billboard_df, 
	id_vars=['year', 'artist.inverted', 'track', 'time', 'genre', 'date.entered', 'date.peaked'], var_name='week', value_name='rank')
print("the molten dataset columns", molten_billboard_df.columns.tolist())

molten_billboard_df['week'] = molten_billboard_df.apply(lambda row: extract_week(row), axis=1)
