def contains_duplicates(arr):
    hash = set()

    for n in arr:
        if n in hash:
            return True

        hash.add(n)

    return False
