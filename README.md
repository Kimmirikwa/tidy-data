# tidy-data
This repo attempts to tidy up untidy data

The following are the properties of a tidy data.
1. Each variable forms a column.
2. Each observation forms a row.
3. Each type of observational unit forms a table.

We therefore to ensure data has the properties above before trying to model using it. Some of the issues of data I am handling here include the following:
* Column headers are values, not variable names.<br/>
I am tidying up data in ```pew.csv``` to have final data which is in ```results.molten_pew.csv```. The code to do this is in ```tidy_pew.py```.<br/>

A section of the original data is shown below, I have ommited a lot of rows and columns. From the table, we can see that except for ```religion```, the rest of the column names are ```values``` instead of ```variables```

| religion  | <$10k | $10-20k | $20-30k |
| --------- | ----- | ------- | ------- |
| Agnostic  | 27    | 34      | 60      |
| Atheist   | 12    | 27      | 37      |
| Buddhist  | 27    | 21      | 30      |

When this data is made by [melting](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html), we have the following final tidy data. The rest of the columns except ```religion``` have been converted to 2 columns, ```income``` and ```frequency```. The data looks narrower and long. The columns are now only variables.

| religion  | income  | frequency |
| --------- | ------- | --------- | 
| Agnostic  | <$10k   | 27        | 
| Atheist   | <$10k   | 12        | 
| Buddhist  | <$10k   | 27        |
| Agnostic  | $10-20k | 34        | 
| Atheist   | $10-20k | 27        | 
| Buddhist  | $10-20k | 21        |
| Agnostic  | $20-30k | 60        | 
| Atheist   | $20-30k | 37        | 
| Buddhist  | $20-30k | 30        |
