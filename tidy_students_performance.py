import pandas as pd

students_performance_df = pd.read_csv('data/students_performance.csv')

# the columns of the dataframe
# id', 'name', 'phone', 'sex and age', 'test number', 'term 1', 'term 2', 'term 3'
print("The columns of the original dataframe", students_performance_df.columns.tolist())