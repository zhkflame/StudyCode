def liner_search(v,L):
    i=0
    while i !=len(L) and L[i]!=v:
        i=i+1
    return 'none' if i==len(L) else i