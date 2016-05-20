class Solution(object):
    def bsearch(self,nums,key,start):
        l=start
        r=len(nums)-1
        while(l<r):
            m=(l+r+1)//2  #+1是为了保证l可以等于r跳出循环
            #print(m)
            if key < nums[m] :
                r=m-1
            else:
                l=m
        if(l==r and nums[l]==key):
            return l
        else:
            return  -1
    def twoSum(self,nums,tar):
        for i in range(0,len(nums)-1):
            res=self.bsearch(nums,tar-nums[i],0)
            if(res!=-1):
                ans=[i,res]
                return ans
    def newTwoSum(self,nums,tar):
        l=0
        r=len(nums)-1
        while(l<r):
            if(nums[l]+nums[r]==tar):
                ans=[l,r]
                return  ans
            elif(nums[l]+nums[r]<tar):
                l=l+1
            else:
                r=r-1
        return -1



res=[1,2,3,4,5,6]
tar=11
my_solution=Solution()
print(my_solution.twoSum(res,tar))

