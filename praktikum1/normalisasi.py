def norm_data(data):
    '''Melakukan normalisasai data.
    
    Parameters:
        data (list): Data yang akan dinormalisasi.
        
    Returns:
        data (list): Data hasil normalisasi.
    '''
    
    data_max = max(data)
    data_min = min(data)
    data_len = len(data)
    
    for i in range (0, data_len):
        data[i] = (data[i] - data_min) / (data_max - data_min)
        
    return data

# Contoh penggunaan
data = [10, 11, 12, 14, 16]
n_data = norm_data(data) # Melakukan Normalisasi
print(n_data)