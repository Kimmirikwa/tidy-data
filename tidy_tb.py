import pandas as pd

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
molten_tb_df = pd.melt(tb_df, id_vars=['iso2', 'year', 'new_sp'], var_name='sex-age', value_name='count')
# The new columns are 'iso2', 'year', 'new_sp', 'age-sex', 'count'
print("The columns for molten data", molten_tb_df.columns)