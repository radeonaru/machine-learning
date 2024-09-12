corpus = ['the house had a tiny little mouse',
          'the cat saw the mouse',
          'the mouse ran away from the house',
          'the cat finally ate the mouse',
          'the end of the mouse story']

from sklearn.feature_extraction.text import TfidfVectorizer

# with open('praktikum1/corpus.txt', 'r') as file:
#     corpus = file.readlines()

#Inisiasi objek TfidfVectorizer
vect = TfidfVectorizer(stop_words='english')

#Pembobotan TF-IDF
resp = vect.fit_transform(corpus)

# Cetak Hasil
print('Hasil Pembobotan TF-IDF')
print(resp)

# Cetak token hasil stopword
print('\nHasil Token')
print(vect.get_feature_names_out())