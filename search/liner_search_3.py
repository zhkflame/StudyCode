def liner_search(v,L):
    L.append(v)
    i=0
    while L[i] != v:
        i=i+1

    L.pop()
    return i