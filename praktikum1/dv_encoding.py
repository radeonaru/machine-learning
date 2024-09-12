from sklearn.preprocessing import OneHotEncoder

de = OneHotEncoder(drop='first')

data = [
    ['Politeknik Negeri Malang'],
    ['Politeknik Elektronika Negeri Surabaya'],
    ['Politeknik Negeri Jakarta'],
    ['Politeknik Negeri Semarang'],
]

transform_de = de.fit_transform(data)

print('Data Asli')
print(data)

print('Data Transformasi One Hot Encoding')
print(transform_de.toarray())