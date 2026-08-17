class Solution(object):
    def separateDigits(self, nums):
        l=[] 
        for i in nums:
          for j in str(i):
            l.append(int(j))
        return(l)