from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder()

data = [
    ['Politeknik Negeri Malang'],
    ['Politeknik Elektronika Negeri Surabaya'],
    ['Politeknik Negeri Jakarta'],
    ['Politeknik Negeri Semarang'],
]

transform_ohe = ohe.fit_transform(data)

print('Data Asli')
print(data)

print('Data Transformasi One Hot Encoding')
print(transform_ohe.toarray())