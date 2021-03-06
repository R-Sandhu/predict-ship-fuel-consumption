import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesRegressor

filePath = '../data/processed/final_features.csv'
df = pd.read_csv(filePath, index_col='Time', parse_dates=True)

# Split-out validation dataset
dataArray = df.values
X = dataArray[:, 1:10]
y = dataArray[:, 0]
validation_size = 0.2
seed = 1
X_train, X_validation, y_train, y_validation = train_test_split(X, y, test_size=validation_size, random_state=seed)

# Test options and evaluation metric
num_folds = 10
seed = 1
scoring = 'neg_mean_squared_error'

scaler = StandardScaler().fit(X_train)
rescaledX = scaler.transform(X_train)

# prepare the model
model = ExtraTreesRegressor(random_state=seed,
                            n_estimators=100,
                            max_features=5,
                            min_samples_split=4,
                            n_jobs=14)
model.fit(rescaledX, y_train)

# transform the validation dataset
rescaledValidationX = scaler.transform(X_validation)
predictions = model.predict(rescaledValidationX)
# print(mean_squared_error(y_validation, predictions))



