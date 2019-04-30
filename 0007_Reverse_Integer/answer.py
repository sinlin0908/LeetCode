class Solution:
    def reverse(self, x: int) -> int:
        tmp = abs(x)
        tmp = int(str(tmp)[::-1])
        
        if tmp < -2**31 or tmp>2**31-1:
            return 0
        elif x<0:
            return tmp*-1
        else:
            return tmp