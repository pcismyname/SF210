def left_join(phrases: tuple) -> str:

    ans = []
    for word in phrases:
        ans.append(word.replace("right","left"))
    print(ans)
    return ",".join(ans)


print(left_join(("left", "right", "left", "stop")))
print()
print(left_join(("brightness wright",)))
print()