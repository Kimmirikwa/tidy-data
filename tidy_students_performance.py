import pandas as pd

students_performance_df = pd.read_csv('data/students_performance.csv')

# the columns of the dataframe
# id', 'name', 'phone', 'sex and age', 'test number', 'term 1', 'term 2', 'term 3'
print("The columns of the original dataframe", students_performance_df.columns.tolist())

# split the dataset to have separate tables for 'student' and 'performance'
# the 2 dataset will have 'id' column, which should be common between them
student_df = students_performance_df[['id', 'name', 'phone', 'sex and age']]
performance_df = students_performance_df[['id', 'test number', 'term 1', 'term 2', 'term 3']]