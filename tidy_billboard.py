import pandas as pd
import re

def extract_week(row):
	week_no = re.findall(r'\d+', row['week'])[0]
	return week_no

billboard_df = pd.read_csv('data/billboard.csv')
print(billboard_df.head())

# the columns of the data
print("The columns of the raw data", billboard_df.columns.tolist())

# sort the dataset by 'artist.inverted'
#billboard_df = billboard_df.sort_values(by=['artist.inverted'])

# add the id column, will ensure song_dataset and rank_dataset share a column
billboard_df['id'] = pd.Series([i for i in range(1, len(billboard_df) + 1)])

# song dataset only has information about the song
song_dataset = billboard_df[['id', 'artist.inverted', 'track', 'time', 'genre']]

# rank dataset has the rest of the information
rank_dataset = billboard_df.drop(['artist.inverted', 'track', 'time', 'genre'], axis=1)

# we start by first melting the dataset
molten_rank_dataset = pd.melt(rank_dataset, 
	id_vars=['id', 'year', 'date.entered', 'date.peaked'], var_name='week', value_name='rank')
print("The molten dataset columns", molten_rank_dataset.columns.tolist())

molten_rank_dataset['week'] = molten_rank_dataset.apply(lambda row: extract_week(row), axis=1)
molten_rank_dataset.sort_values(by=['id', 'date.entered'], inplace=True)

# create files for the tidy datasets
song_dataset.to_csv('results/tidy_billboard_songs.csv', index=False)
molten_rank_dataset.to_csv('results/tidy_billboard_rank.csv', index=False)
