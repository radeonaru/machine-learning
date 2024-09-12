import numpy as np
from sklearn.preprocessing import StandardScaler

np.set_printoptions(precision=6)
np.set_printoptions(suppress=True)

data = [
    [100, 0.0001],
    [50, 0.05],
    [30, 0.003]
]

data = np.asarray(data)
print('Data Asli')
print(data)

scaler = StandardScaler()

scaled = scaler.fit_transform(data)
print('Data Standarisasi')
print(scaled)