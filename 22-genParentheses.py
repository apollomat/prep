class Solution(object):
    
    def genPerms(self,n, res, curr, open_i, close_i):
        if(open_i + close_i == n):
            res.append(curr)
            return
        else:
            if open_i < n/2:
                self.genPerms(n, res, curr + '(', open_i + 1, close_i)
            if close_i < open_i:
                self.genPerms(n, res, curr + ')', open_i, close_i + 1)
        
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        curr =""
        if(n == 0):
            return res
        
        self.genPerms(n*2, res, curr, 0, 0)
        return res
