class Solution :
    def twoSum(self ,nums , target) :
        dict={}
        n=len(nums)
        for i in range(n):
            dict[nums[i]]=i
        for i in range(n):
            c = target - nums[i]
            if c in dict and dict[c] != i:
                return[i,dict[c]]
        return[]
     
                                        