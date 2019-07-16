from stack import Stack

def is_matched(p2, p):
    if p2 == '(' and p == ')':
        return True
    elif p2 == '{' and p == '}':
        return True
    elif p2 == '[' and p ==']':
        return True
    else:
        return False

def is_paren_balanced(paren):
    stack = Stack()
    is_balanced = True
    index = 0
    
    while index < len(paren) and is_balanced:
        p = paren[index]
        if p in '({[':
            stack.push(p)
        else:
            if stack.is_empty():
                is_balanced = False
            else:
                p2 = stack.pop()
                if not is_matched(p2, p):
                    is_balanced = False
        index += 1
    if is_balanced:
        return True
    else: 
        return False






print(is_paren_balanced("(((({}))))"))

print(is_paren_balanced("[][]]]"))
print(is_paren_balanced("[][]"))


