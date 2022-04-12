import itertools

FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

permutations = list(itertools.combinations(FLAVORS, r=2))

#print((permutations))

for i in permutations:
    i=str(i)
    i= i.replace("'", "")
    i= i.replace("(", "")
    i= i.replace(")", "")
    print(i)
