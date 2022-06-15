def backward_string_by_word(text: str) -> str:
    stack = []
    ans = ""
    for i in range(len(text)):
        if text[i] != " ":
            stack.append(text[i])
        else :
            while len(stack) > 0:
                ans += stack[-1]
                stack.pop()
            ans += " "
    while len(stack) > 0:
            ans += stack[-1]
            stack.pop()
    return ans


print(backward_string_by_word('hello   world') )

