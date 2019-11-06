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

* Multiple variables stored in one column <br/>
The following dataset has this issue

| iso2  | year | new_sp | new_sp_m04 | new_sp_m514 | new_sp_m014 | new_sp_f014
| --------- | ----- | ------- | ------- | ------- | ------- | ------- |
| AD  | 1989    |      |       |       |||
| AD   | 1990    |       |       |        |||
| AD  | 1991    |       |       |       |||


The table above show just a few rows and columns of the dataset. The columns ```new_sp_m04```, ```new_sp_m514```, ```new_sp_m014``` and the rest of the columns chown here have store more than one variable i.e ```new_sp```, ```sex``` and ```age```. For example, ```new_sp_m04``` has ```sex``` as ```m``` for male, ```04``` which is ages ```0-4```. At the moment I am not sure what ```new_sp``` stands for. Therefore I will only extract ```sex``` and ```age``` from relevant columns.

I start by melting the dataset to have ```iso2```, ```year```, ```new_sp```, ```sex-age```(with the rest of the columns as values) and ```count```(with the initial values of the converted column values)

I then extract ```sex``` and ```age``` values and I add them to the relevant columns. The code for this is in ```tidy_tb.py```. The final tidy file is in ```results/tidy_tb.csv```.
Below is part of the tidy data(for the above part of the initial of the initial table)

| iso2  | year | new_sp | sex | age | count |
| --------- | ----- | ------- | ------- | ------- | ------- |
| AD  | 1989    |      |    m   |    0-4   ||
| AD   | 1990    |       |  m     |    5-14    ||
| AD  | 1991    |       |    m   |     0-14  ||
| AD  | 1991    |       |    f   |     0-14  ||
