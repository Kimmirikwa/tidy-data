import pandas as pd

def get_sex_and_age(row):
	sex_and_age = row['sex and age'].split('_')
	sex = sex_and_age[0]
	age = sex_and_age[1]

	sex = 'male' if sex == 'm' else 'female'

	return pd.Series([sex, age])

students_performance_df = pd.read_csv('data/students_performance.csv')

# the columns of the dataframe
# id', 'name', 'phone', 'sex and age', 'test number', 'term 1', 'term 2', 'term 3'
print("The columns of the original dataframe", students_performance_df.columns.tolist())

# split the dataset to have separate tables for 'student' and 'performance'
# the 2 dataset will have 'id' column, which should be common between them
student_df = students_performance_df[['id', 'name', 'phone', 'sex and age']]
performance_df = students_performance_df[['id', 'test number', 'term 1', 'term 2', 'term 3']]

# for student_df, the 'sex and age' column needs to be split into 2
student_df[['sex', 'age']] = student_df.apply(lambda row: get_sex_and_age(row), axis=1)
# dropping the 'sex and age' column
student_df.drop(['sex and age'], axis=1, inplace=True)

# drop duplicates
student_df.drop_duplicates(['id'], keep='first', inplace=True)

student_df.to_csv('results/tidy_students.csv', index=False)

# now dealing with the performance data
# we first melt the data to have 'term 1', 'term 2' and 'term 3' in their own columns
molten_performance_df = pd.melt(performance_df, id_vars=['id', 'test number'], var_name='term', value_name='marks')