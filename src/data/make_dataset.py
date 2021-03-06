import pandas as pd
from csv import reader


def load_csv(filename):
    """
    Load data from a csv file

    Parameters
    ----------
    filename: str
      Complete path of input dataset

    Returns
    -------
    List
      List of lists where each element represents a single record
    """
    dataset = list()
    with open(filename, "r") as f:
        csv_reader = reader(f)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset


def time_index(data, col_ts, ts_units):
    """
    Convert unix ts to date-time and re-index data-frame

    Parameters
    ----------
    data: Pandas DataFrame
      Input pandas data frame object
    col_ts: str
      Column name with timestamp data
    ts_units: str
      Units of the timestamp. This could be 's' as seconds, refer to documentation for more options.

    Returns
    -------
    DataFrame
      Pandas DataFrame object with dateTime index
    """
    data[col_ts] = pd.to_datetime(data[col_ts], unit=ts_units)
    data.set_index(col_ts, inplace=True)
    return data


def rename_cols(data, new_col_names):
    """
    Rename columns
    """
    data.columns = new_col_names
    return data


fileName = '.../data/raw/ship_data.csv'
dataset = load_csv(fileName)
print("Loaded data with {0} rows and {1} columns".format(len(dataset), len(dataset[0])))

# Convert to pandas dataframe
colNames = dataset[0]
df = pd.DataFrame(dataset[1:], columns=colNames)

df = time_index(df, 'Time', 's')
new_col_names = ['fuelConsumption', 'HFO', 'MGO', 'draftForward', 'draftAft', 'draftMid1', 'draftMid2',
              'shaftSpeed', 'shaftTorque', 'shaftPower', 'speedGround', 'speedWater', 'heading', 'rudderAngle',
              'AWS', 'AWD', 'TWS', 'TWD', 'temp', 'currentDirection', 'currentSpeed', 'waterDepth', 'waveHeight',
              'wavePeriod', 'waveDirection']

df = rename_cols(df, new_col_names)

df = df.replace(r'^\s*$', np.nan, regex=True).astype(np.float64)

# Drop null values and select features
df.dropna(how='any', inplace=True)

df.dropna(how='any', inplace=True)

df['meanDraft'] = df[['draftAft', 'draftForward', 'draftMid1', 'draftMid2']].mean(axis=1)

cols_to_drop = ['MGO', 'draftForward', 'draftAft', 'draftMid1', 'draftMid2', 'shaftTorque', 'shaftPower',
                'speedGround', 'AWS', 'AWD', 'currentDirection', 'currentSpeed', 'waterDepth',
                'waveHeight', 'wavePeriod', 'waveDirection']

df.drop(columns=cols_to_drop, inplace=True)

# Remove data anomalies
conditionEval = (df['heading'] < 0) | (df['temp'] < -273) | (df['fuelConsumption'] < -0.5)
df.drop(df[conditionEval].index, inplace=True)

df.loc[df['fuelConsumption'] < 0, 'fuelConsumption'] = 0


