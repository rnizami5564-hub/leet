def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            s=nums[i]+nums[j]
            if s==target:
             print(i,j,s)
             break
twoSum([10,4,1,5,3,6],10)
 
  