import pandas as pd

def extract_year(row):
	year = str(row['year'])
	month = str(row['month'])
	month = '0' + month if len(month) == 1 else month  # handle months less than October
	day = row['day'][1:]  # get rid of leading 'd'
	day = '0' + day if len(day) == 1 else day

	return '-'.join([year, month, day])

def get_max_min(dataset, row):
	date = row['date']
	element = row['element']
	value = row['value']
	tmax_item = dataset.loc[(dataset['date'] == date) & (dataset['element'] == 'tmax')].iloc[0]
	tmin_item = dataset.loc[(dataset['date'] == date) & (dataset['element'] == 'tmin')].iloc[0]
	tmax = tmax_item['value']
	tmin = tmin_item['value']
	return pd.Series([tmax, tmin])

weather_df = pd.read_csv('data/weather.csv')

# 'id', 'year', 'month', 'element', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13', 
# 'd14', 'd15', 'd16', 'd17', 'd18', 'd19', 'd20', 'd21', 'd22', 'd23', 'd24', 'd25', 'd26', 'd27', 'd28', 'd29', 'd30', 'd31'
# we will need to melt this dataset. We will retain 'id', 'year', 'month' and 'element'.
# The rest of the columns will be converted to 2 columns i.e 'day' and 'value' 
print("The original columns", weather_df.columns.tolist())

molten_weather_df = pd.melt(weather_df, id_vars=['id', 'year', 'month', 'element'], var_name='day')
print("The molten columns", molten_weather_df.columns.tolist())  # 'id', 'year', 'month', 'element', 'day', 'value'

# next we extract 'date' by combining 'year', 'month' and 'day'
molten_weather_df['date'] = molten_weather_df.apply(lambda row: extract_year(row), axis=1)

# create 'tmax' and 'tmin'
molten_weather_df[['tmax', 'tmin']] = molten_weather_df.apply(lambda row: get_max_min(molten_weather_df, row), axis=1)

# drop redundant columns
molten_weather_df.drop(['year', 'month', 'day', 'element', 'value'], axis=1, inplace=True)

# unfortunately we have duplicate entries for all observations.
# we therefore retain only one observation per day
molten_weather_df.drop_duplicates('date', keep='first', inplace=True)

# sort the dataset by 'date'
molten_weather_df.sort_values(by=['date'], inplace=True)
