
def sequential_search(list_, n):
    found = False
    for i in list_:
        if i == n:
            found = True
            break
    return found
