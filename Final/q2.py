def is_balance(data):
    stack = []
    open = ["(", "{", "["]
    close = [")", "}", "]"]
    braces = open + close
    for i in data:
        if i not in braces:
            continue
        if i in braces and len(data) == 1:
            return False
        if i in open:
            if not stack and data.index(i) == len(data)-1:
                return False
            stack.append(i)
        else:
            if not stack and i in close:
                return False
            current = stack.pop()
            if current == "(" :
                if i != ")":
                    return False
            if current == "[" :
                if i != "]":
                    return False
            if current == "{" :
                if i != "}":
                    return False
    return True
    
print(is_balance("if a(4) > 9: { foo(a[2]) }"))
print(is_balance("for (i=0i&lta(3}i += 1): foo{) )"))
print(is_balance("for (i=0i&lta(3}i += 1): foo{) )"))
print(is_balance("while True) foo() }{ ()"))
print(is_balance("if x:"))
print(is_balance(""))
print(is_balance("}{"))
print(is_balance("if (x) (})"))
print(is_balance("if (x) {"))
print(is_balance("(({{}}){}{}())"))
