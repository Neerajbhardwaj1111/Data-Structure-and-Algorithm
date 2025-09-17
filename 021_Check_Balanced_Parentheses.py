'''
Valid Parentheses in an Expression

Given a string s containing three types of brackets {}, () and []. Determine whether the Expression are balanced or not.
An expression is balanced if each opening bracket has a corresponding closing bracket of the same type, the pairs are properly ordered and no bracket closes before its matching opening bracket.

Balanced: "[()()]{}" → every opening bracket is closed in the correct order.
Not balanced: "([{]})" → the ']' closes before the matching '{' is closed, breaking the nesting rule.
Example: 

Input: s = "[{()}]"
Output: true
Explanation:  All the brackets are well-formed.

Input:  s = "([{]})"
Output: false
Explanation: The expression is not balanced because there is a closing ']' before the closing '}'.
'''

s = '[{()}]'
stack =[]
res = 1
for ele in s:
    if ele in ('[','{','(') :
        stack.append(ele)
    else:
        if ele == ']':
            if stack[-1]== '[':
                stack.pop()
            else:
                res =0
        elif ele == '}':
            if stack[-1]== '{':
                stack.pop()
            else:
                res =0
        elif ele == ')':
            if stack[-1]== '(':
                stack.pop()
            else:
                res =0
    print(stack)


print("True" if len(stack)==0 else "False")
