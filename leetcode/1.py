def canBeValid(s, locked):
        op, cl = 0, 0
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                if locked[i] == 0:
                    op += 1
                stack.append(s[i])
            else:
                if not stack and locked[i] == '0':
                    stack.append('(')
                    cl += 1
                elif not stack:
                    return False
                else:
                    stack.pop()
        if stack:
            if op == cl:
                return True
            if len(stack) <= op:
                return True
            else:
                return False
        return True

canBeValid("))()))", "010100")