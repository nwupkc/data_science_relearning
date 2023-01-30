# pandas is a helpful data analysis tool
import pandas as pd


# read in data as a dataframe
df = pd.read_csv('../input/dataset_name.csv')

# view first five rows
df.head()

# view last five rows
# I usually check this to see if data behaves the way I expect it to till the last row.
df.tail()
# you can specify number of rows to display
df.tail(10)

# list column names
df.columns

# pull up summary statistics
df.describe()