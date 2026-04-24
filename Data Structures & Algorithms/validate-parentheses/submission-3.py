class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False

        opmap = {')': '(', '}':'{', ']':'['}
        stack = []
        for c in s:
            if c in opmap.values():
                stack.append(c)
                continue

            if len(stack):
                if c in opmap.keys():
                    if stack[-1] == opmap[c]:
                        stack.pop()
                    else: break
            else:
                return False
        
        return True if len(stack) == 0 else False
                
            
        