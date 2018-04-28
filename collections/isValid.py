def isValid(s):
        dt = {')': '(', ']': '[', '}': '{'}   
        stack = []                            
        for char in s:
            if char not in dt:              
                stack.append(char)
                print stack
            else:
                if len(stack) == 0 or stack.pop() != dt[char]:
                    print stack
                    return False 

        return True if len(stack) == 0 else False

print isValid('()')
            