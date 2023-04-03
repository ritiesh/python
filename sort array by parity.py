class Solution(object):
    def sortArrayByParity(self, nums):
        m=[]
        for i in range(len(nums)):
            if(nums[i]%2==0):
                m.append(nums[i])
        for i in range(len(nums)):
            if(nums[i]%2!=0):
                m.append(nums[i])
        return m
