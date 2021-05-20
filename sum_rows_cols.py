import pandas as pd
import numpy as np

# Create a dataframe
d = {'type': ['X', 'X', 'Z', 'Y', 'X', 'X', 'Y', 'Y'],
     'number': [3, 4, 6, 2, 6, 9, 10, 5],
     'number2': [6, 5, 0, 1, 3, 3, 4, 10]}

df = pd.DataFrame(data=d)

'''
# This calculates the sum of a specific column
df.loc["Total", "number"] = df.number.sum()
df.loc["Total", "number2"] = df.number2.sum()
print (df)

# This sums data row by row
df["sum"] = df.sum(axis=1)
print (df)


# This calculate the sum of each distinct value
df_sum_number = df.groupby('type')['number'].sum()
df_sum_number2 = df.groupby('type')['number2'].sum()
print (df_sum_number2)

# This calculate the sum of specific value
df_sum_X_number = df.loc[df['type'] == 'X', 'number'].sum()
print (df_sum_spec_number)
'''
total = np.sum(df.loc['number'].values)
print (total)
#df['percent'] = df.ix[:,'number':].sum(axis=1)/total * 100
#print (df)