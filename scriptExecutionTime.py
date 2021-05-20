
from datetime import datetime,timedelta
import pandas as pd
import numpy as np


startTime = datetime.now()

file = r'F:\tko_root\GIS_WORKSPACE\MLABIADH\PyMe\pandas_test\bcts_tko_harvested_2016_2019.csv'
df = pd.read_csv(file)

#number of rows and cols
row, col = df.shape

print (row,col)

# Extract columns and rows based on index
x = df.iloc[:,3:10] # Retrieve all rows and columns from 3 to 10

# Extract columns based on name
y = df[['LICENCE_ID', 'BLOCK_ID']]

# Arithmetics using two clolumns

## Remove comma thousand seperator and convert to float
df["MAX_ELEVAT"]= df["MAX_ELEVAT"].replace(',', '',regex=True).astype(float)
df["MIN_ELEVAT"]= df["MIN_ELEVAT"].replace(',', '',regex=True).astype(float)


## Calculate average of  2 columns
df['AVG_ELEVAT'] = (df['MIN_ELEVAT'] + df['MAX_ELEVAT']) / 2

# Extract rows based on value
e = df.where (df['MANU_ID'] == 'Cascadia')


#replace values based on a condition
import numpy as np
df['condition'] = np.where((df['MANU_ID'] == 'Cascadia'), 
                           1, 
                           0) 

endTime = datetime.now()
processTime = endTime - startTime

print (processTime)

print ('Processing Completed! It took {} (HH:MM:SS)'. format(round(processTime)))
