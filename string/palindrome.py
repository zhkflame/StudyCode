def isPalindrome(s):
    lth=len(s)
    l,r=0,lth-1
    while(l<r):
        while(l<r and not s[l].isdigit() and not s[l].isalpha()):
            l=l+1
        while(l<r and not s[r].isdigit() and not s[r].isalpha()):
            r=r-1
        if(s[l].lower()==s[r].lower()):
            l,r=l+1,r-1
        else:
            return False
    return True
if __name__=="__main__":
    a='a,bc,cbA'
    b='abc;dcba'
    c='sdlfk'
    print(isPalindrome(a))
    print(isPalindrome(b))
    print(isPalindrome(c))
    print(isPalindrome(','))