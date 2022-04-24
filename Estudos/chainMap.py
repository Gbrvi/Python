def chain(*iters):
    for l in iters:
        print(l)

print(chain([1, 2, 3, 4, 5], [5, 6, 7, 8]))