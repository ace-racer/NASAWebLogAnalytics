import pandas as pd
import os

os.chdir('C:\\Users\\pierl\\PycharmProjects\\NASA\\association_analysis')
df = pd.read_csv('nasa_data\\sessionized_data\\sessionize_hostonly_july_ordered.csv')

count = 1
prev_seqid = 1
processed_df = df
processed_df = processed_df.iloc[0:0]

for idx, row in df.iterrows():
    # print('.')
    if row['sequenceID'] != prev_seqid:
        count = 1

    row['eventID'] = count
    prev_seqid = row['sequenceID']
    processed_df = processed_df.append(row)
    count = count + 1

processed_df.to_csv('hostonly_july_ordered.csv')
