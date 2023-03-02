class Solution:    
    @functools.lru_cache(None)
    def diffWaysToCompute(self, s):
        if len(s) <= 2: return [int(s)]
        vals = []
        for i,x in enumerate(s):
            if x in '+-*':
                vals += [eval(f"{left}{x}{right}") for left in self.diffWaysToCompute(s[:i]) 
                         for right in self.diffWaysToCompute(s[i+1:])]
        return vals








