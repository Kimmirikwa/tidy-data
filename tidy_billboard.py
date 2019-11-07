import pandas as pd
import re

def extract_week(row):
	week_no = re.findall(r'\d+', row['week'])[0]
	return week_no

billboard_df = pd.read_csv('data/billboard.csv')

# the columns of the data
print("The columns of the raw data", billboard_df.columns.tolist())

# song dataset only has information about the song
song_dataset = billboard_df[['artist.inverted', 'track', 'time', 'genre']]

# rank dataset has the rest of the information
rank_dataset = billboard_df.drop(['artist.inverted', 'track', 'time', 'genre'], axis=1)

# we start by first melting the dataset
molten_rank_dataset = pd.melt(rank_dataset, 
	id_vars=['year', 'date.entered', 'date.peaked'], var_name='week', value_name='rank')
print("the molten dataset columns", molten_rank_dataset.columns.tolist())

molten_rank_dataset['week'] = molten_rank_dataset.apply(lambda row: extract_week(row), axis=1)
