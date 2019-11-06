import pandas as pd

weather_df = pd.read_csv('data/weather.csv')

# 'id', 'year', 'month', 'element', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13', 
# 'd14', 'd15', 'd16', 'd17', 'd18', 'd19', 'd20', 'd21', 'd22', 'd23', 'd24', 'd25', 'd26', 'd27', 'd28', 'd29', 'd30', 'd31'
# we will need to melt this dataset. We will retain 'id', 'year', 'month' and 'element'.
# The rest of the columns will be converted to 2 columns i.e 'day' and 'value' 
print("The original columns", weather_df.columns.tolist())

molten_weather_df = pd.melt(weather_df, id_vars=['id', 'year', 'month', 'element'], var_name='day')
print("The molten columns", molten_weather_df.columns.tolist())  # 'id', 'year', 'month', 'element', 'day', 'value'
