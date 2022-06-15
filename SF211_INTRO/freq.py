def frequency_sort(items):
    # your code here
    freq =  dict()
    ans = []
    for i in items:
        freq[i] = items.count(i)
    sort_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    for i in sort_freq:
        for j in range(i[1]):
            ans.append(i[0])
    return ans


print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
print(frequency_sort(['carl', 'alex', 'bob','bob', 'bob', ]))



