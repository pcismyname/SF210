def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    ans = []
    all = []
    for i in data:
        all.append(i["price"])
    all = sorted(all)
    #print(all)
    for i in range(limit):
        for j in data:
            if j["price"] ==  all[len(data)-i-1]:
                ans.append(j)
    return ans



print(bigger_price(2, [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]))