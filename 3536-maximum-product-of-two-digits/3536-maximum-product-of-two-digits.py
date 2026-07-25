class Solution:
    def maxProduct(self, n: int) -> int:
        first,second = 0,0
        while n > 0:
            d = n%10
            if d > first:
                first,second = d,first
                print(first)
            elif d > second:
                second = d 
                print(second)
            n = n//10
        prod = first * second 
        return prod
        

        


        