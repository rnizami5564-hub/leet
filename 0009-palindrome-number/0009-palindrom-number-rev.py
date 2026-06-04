class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        rev=0
        num=x
        while num>0:
            d=num%10
            rev= rev*10 + d
            num//=10
        return rev == x
        
