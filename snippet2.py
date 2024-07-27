def sort_by_indices(lst, idx, rev=False):
    return [val for(val, _) in sorted(zip(lst,idx), key = lambda x : x[1], reverse=rev)]

a = ['eggs', 'bread', 'oranges', 'jam', 'apples', 'milk']
b = [3, 2, 6, 4, 1, 5]
print(sort_by_indices(a, b))
print(sort_by_indices(a, b, True))