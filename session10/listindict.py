Film = {
    'name': 'Up',
    'year': 1998,
    'cast': ['Russell', 'Grand', 'Elle'],
    'script': 'a married couple dreams about going to Heaven Water Fall someday and they had an amazing adventure'
}

key = 'editor'
value = 'ABC'
Film[key] = value
print(Film)

Film['cast'].append('Kid')
print(Film)

for k,v in Film.items():
    print(k, v, sep='-')