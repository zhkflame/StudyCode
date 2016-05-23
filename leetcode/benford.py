import matplotlib.pyplot as plt

def first_num(n):
    while n>=10:
        n=n//10
    return n
def second_num(n):
    while n>=100:
        n=n//10
    return n%10
def third_num(n):
    while n>=1000:
        n=n//10
    return n%10

if __name__ =="__main__":
    n=1
    frequency=[0 for x in range(10)]
    print(frequency)
    for i in range(1,10000,1):
        if n>1000000000000:
            n=n//1000000000
        n=n*i
        m=first_num(n)
        frequency[m]=frequency[m]+1
    print(frequency)
    plt.plot(frequency,"r-",linewidth=2)
    plt.plot(frequency,"go",markersize=8)
    plt.grid(True)
    plt.show()