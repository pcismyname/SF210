def check_balance(str):
    stack =  []
    stack_index = []
    open = ["(", "{", "["]
    close = [")", "}", "]"]
    braces = open + close
    for i in str:
        if i not in braces:
            continue
        if i in open :
            if not stack and str.index(i) == len(str)-1 :
                return len(str)
            stack.append(i)
            
        else :
            if not stack and i in close:
                return str.index(i)
            cur = stack.pop()
            if cur == "(" :
                if i != ")":
                    return str.index(i)
            if cur == "[" :
                if i != "]":
                    return str.index(i)
            if cur == "{" :
                if i != "}":
                    return str.index(i)
    return -1


a=check_balance("if (x) {")
print(a)