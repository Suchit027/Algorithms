def reverseParentheses(s):
    def helper(s):
        ret = ''
        i = 0
        while i < len(s):
            if s[i] != '(':
                ret = s[i] + ret
            else:
                i += 1
                a = ''
                op = 1
                while op > 0:
                    if s[i] == '(':
                        op += 1
                    elif s[i] == ')':
                        op -= 1
                    else:
                        a = a + s[i]
                    i += 1
                add = helper(a)
                ret = add[:: -1] + ret
        return ret

    return helper(s)

print(reverseParentheses('(abcd)'))