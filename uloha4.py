import math

def calculate_subarray_sums(inp):
    sums = []
    for i in range(len(inp)):
        for j in range(i + 2, len(inp) + 1):
            sums.append(sum(inp[i:j]))
    
    sumset = tuple(set(sums))
    multiples = [[num] * sums.count(num) for num in sumset if sums.count(num) > 1]
    
    res = 0
    for i in multiples:
        res += len(i) * (len(i) - 1) // 2
    
    return res

# Příklad použití
inp = [1, 2, 3, 4, 5]
result = calculate_subarray_sums(inp)
print(f"Výsledek: {result}")