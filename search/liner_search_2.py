def liner_search(v,L):
    i=0
    for value in L:
        if v==value:
            return i
        i=i+1
    return len(L)
