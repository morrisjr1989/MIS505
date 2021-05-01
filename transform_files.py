import pandas as pd
import glob

pattern = glob.glob("./data/*.csv")

_frames = []
for file in pattern:

    df = pd.read_csv(file)
    
    year = file.split("\\")[1][2:6]
    idx = ['Mode', 'NLC', 'ASC', 'Station', 'Coverage', 'Source']

    df = df.set_index(idx)
    df = df.stack().reset_index()
    df[['type', 'day']] = df['level_6'].str.split("|", expand=True)
    df = df.drop('level_6', axis=1)
    df = df.rename({
        0: 'count'
    }, axis=1)

    df['year'] = year
    
    _frames.append(df)

main_df = pd.concat(_frames)

main_df.to_csv('combained_years_tu.csv', index=False)