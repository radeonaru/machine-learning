from sklearn.preprocessing import OrdinalEncoder

oe = OrdinalEncoder()

data = [
    ['Politeknik Negeri Malang'],
    ['Politeknik Elektronika Negeri Surabaya'],
    ['Politeknik Negeri Jakarta'],
    ['Politeknik Negeri Semarang']
]

transform_oe = oe.fit_transform(data)

print('Data Asli')
print(data)

print('Data Transformasi Ordinal Encoder')
print(transform_oe)