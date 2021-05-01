import pandas as pd
import glob

# glob to read in csv files in data folder
pattern = glob.glob("./data/*.csv")

# generate frames list for the concat
_frames = []
for file in pattern:
   # read dataframe from file
    df = pd.read_csv(file)
   # get the file year to use for new file name 
   # generate idx based upon headers
    year = file.split("\\")[1][2:6]
    idx = ['Mode', 'NLC', 'ASC', 'Station', 'Coverage', 'Source']
    df = df.set_index(idx)
    
    # stack data and reset index - split along combined multi-index  drop and rename
    df = df.stack().reset_index()
    df[['type', 'day']] = df['level_6'].str.split("|", expand=True)
    df = df.drop('level_6', axis=1)
    df = df.rename({
        0: 'count'
    }, axis=1)

    df['year'] = year
    
    # add this dataframe to frames
    _frames.append(df)

 # concat all frames into main
main_df = pd.concat(_frames)

 # export as csv for tableau and make sure to spell it weird.
main_df.to_csv('combained_years_tu.csv', index=False)
