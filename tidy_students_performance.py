import pandas as pd

def get_sex_and_age(row):
	sex_and_age = row['sex and age'].split('_')
	sex = sex_and_age[0]
	age = sex_and_age[1]

	sex = 'male' if sex == 'm' else 'female'

	return pd.Series([sex, age])

def get_term_no(row):
	return row['term'][-1]

def get_marks_for_tests(dataset, row):
	student_id = row['id']
	term = row['term']
	test1_observation = dataset.loc[(dataset['id'] == student_id) & (dataset['term'] == term) & (dataset['test number'] == 'test 1')].iloc[0]
	test2_observation = dataset.loc[(dataset['id'] == student_id) & (dataset['term'] == term) & (dataset['test number'] == 'test 2')].iloc[0]

	test1_marks = test1_observation['marks']
	test2_marks = test2_observation['marks']

	return pd.Series([test1_marks, test2_marks])

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

# extracting term number
molten_performance_df['term'] = molten_performance_df.apply(lambda row: get_term_no(row), axis=1)

# marks for each term
molten_performance_df[['test 1 marks', 'test 2 marks']] = molten_performance_df.apply(
	lambda row: get_marks_for_tests(molten_performance_df, row), axis=1)

# drop redundant 'marks' column
molten_performance_df.drop(['marks'], axis=1, inplace=True)

# drop duplicates
molten_performance_df.drop_duplicates(['id', 'test number', 'term'], keep='first', inplace=True)
