import matplotlib.pyplot as plt

def first_num(n):
    while n>10:
        n=n//10
    return n

print first_num(7845)