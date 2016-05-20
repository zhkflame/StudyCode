

class Solution(object):
    def twoSum(self, nums, target):
        """----三个引号表示注释内容
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer={}
        for i in range(0,len(nums)):
            x=nums[i]
            if(target-x in answer):
                res=[answer.get(target-x),i]
                return res
            answer[x]=i
    def bsearch(self,nums,key,start):
        l=start
        r=len(nums)
        while(l<=r):
            m=(l+r)/2
            if nums[m]==key :
                return m
            elif nums[m] < key:
                l=m+1
            else:
                r=m-1
        return -1

def twoSum(nums, target):
    answer={}
    for i in range(0,len(nums)):
        x=nums[i]
        if(target-x in answer):
            res=[answer.get(target-x),i]
            return res
        answer[x]=i
nums=[4,2,5,7,9]
print(twoSum(nums,17))