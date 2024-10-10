animals = ["cat", "dog", "bird"]
pawslist = [4, 4, 2]
is_vactibated = [False, True, False]

'''
  | type  | paws | is_vactinated
0 | dog   |  4   | True
1 | cat   |  4   | False
2 | goose |  2   | True

'''

animal_list = [
    {"type": "dog", "paws": 4, "is_vactinated": True},
    {"type": "cat", "paws": 4, "is_vactinated": False},
    {"type": "bird", "paws": 2, "is_vactinated": False}
]

#print(animal_list)

for animal in animal_list:
    print(animal)
    for item in animal:
        print(item, " ",animal[item])