import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier



x = pd.read_csv('mac2.csv')
y = x.pop("mobiledevice")
numeric_variables = list(x.dtypes[x.dtypes != "object"].index)
# x[numeric_variables].head()
model = randomforestclassifier(n_estimators=100, oob_score=True, random_state=42)
model = fit(x[numeric_variables], y)

test=
print(x)
