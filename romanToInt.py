class Solution(object):
    def romanToInt(self, s):
        T = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        val = 0
        for i in range(0,len(s)):

            if(i < len(s) - 1 and T[s[i]] < T[s[i+1]]):
                val -= T[s[i]]
            else:
                val += T[s[i]]
        return val    
        
