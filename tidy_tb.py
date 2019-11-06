import pandas as pd

def extract_sex(row):
	# sex if either 'm' or 'f' and is always the 7th value of 'sex-age'
	return row['sex-age'][7]

def extract_age(row):
	# age is found from 8th value of 'sex-age' onwards
	age = row['sex-age'][8:]
	if not age.isdigit():  # for 'u' which is undefined
		return age
	hiphen_position = len(age) // 2
	age = '-'.join([age[:hiphen_position], age[hiphen_position:]])
	return age

tb_df = pd.read_csv('data/tb.csv')

# the following are the columns of the data
# 'iso2', 'year', 'new_sp', 'new_sp_m04', 'new_sp_m514', 'new_sp_m014',
# 'new_sp_m1524', 'new_sp_m2534', 'new_sp_m3544', 'new_sp_m4554',
# 'new_sp_m5564', 'new_sp_m65', 'new_sp_mu', 'new_sp_f04', 'new_sp_f514',
# 'new_sp_f014', 'new_sp_f1524', 'new_sp_f2534', 'new_sp_f3544',
# 'new_sp_f4554', 'new_sp_f5564', 'new_sp_f65', 'new_sp_fu'
# m -> male, f -> female, 514 -> 5 - 14
print("The original columns", tb_df.columns)

# we will first melt this data to convert all other columns except 'iso2', 'year', and 'new_sp' to 2 columns
# next will extract sex and age from the created variable column to and add the values to respective columns

# melting the data
molten_tb_df = pd.melt(tb_df, id_vars=['iso2', 'year', 'new_sp'], var_name='sex-age', value_name='count')
# The new columns are 'iso2', 'year', 'new_sp', 'age-sex', 'count'
print("The columns for molten data", molten_tb_df.columns)

# sorting the data
molten_tb_df.sort_values(by=['iso2', 'sex-age', 'year'], inplace=True)

# finally we extract sex and age from 'sex-age'
molten_tb_df['sex'] = molten_tb_df.apply(lambda row: extract_sex(row), axis=1)
molten_tb_df['age'] = molten_tb_df.apply(lambda row: extract_age(row), axis=1)
