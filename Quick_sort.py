def quicksort(liste):
    if len(liste) <= 1:
        return liste
    else:
        return quicksort(filter(lambda x: x < liste[0], liste[1:])) + \
               [ liste[0] ] + \
               quicksort(filter(lambda x: x >= liste[0], liste[1:]))

L=[1,3,4,7,9,8]
print quicksort(L)
