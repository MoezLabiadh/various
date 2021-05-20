import pandas as pd

file = r'\\bctsdata.bcgov\data\tko_root\GIS_WORKSPACE\MLABIADH\GIS-REQUESTS\ong-20210422-timber_analysis_FN_PETER\results\summary_stats_20210513.xlsx'
df = pd.read_excel(file)

'''
df['Total Op Area Volume'] = 0.0

grouped = df.groupby(['Operating Area'])['Volume (m3)'].max()

for index, row in df.iterrows():
    for value in grouped.iteritems():
        if str(row['Operating Area']) == str(value[0]):
            df.at[index,'Total Op Area Volume'] = value[1]

'''


AAC_dict = {
"Arrow": 500000,
"Cascadia": 346920,
"Boundary": 670142,
"Cranbrook": 808000,
"Golden": 485000,
"Invermere": 496720,
"Kootenay Lake": 634861,
"Okanagan": 3078405,
"Revelstoke": 225000
}


for index, row in df.iterrows():
    for key, value in AAC_dict.items():
        if row['TSA'] == key:
            df.at[index,'AAC (m3/year)'] = value

df["AAC per FN"] = (df['Volume (m3)'] / df['Total Op Area Volume']) *  df['AAC (m3/year)']

print (df.head(5))

output = r'\\bctsdata.bcgov\data\tko_root\GIS_WORKSPACE\MLABIADH\GIS-REQUESTS\ong-20210422-timber_analysis_FN_PETER\results\summary_stats_20210514.xlsx'
df.to_excel(output)