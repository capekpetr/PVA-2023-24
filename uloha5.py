import math

def calculate_subarray_sums(inp):
    distances = []
    planes = []
    for i in range(len(inp)):
        for j in range(i + 1, len(inp)):
            planes.append([inp[i][2], inp[j][2]])
            distances += (abs(inp[i][0] - inp[j][0]) ** 2 + abs(inp[i][1] - inp[j][1]) ** 2) ** 0.5,
    
    min_distance = min(distances)
    indices = [i for i, dist in enumerate(distances) if dist == min_distance]
    
    print(f"Minimum distance: {min_distance}")
    print("Pairs of planes with minimum distance:")
    for i in indices:
        print(planes[i])

# Příklad použití
inp = [
    [1.0, 2.0, "A"],
    [3.0, 4.0, "B"],
    [5.0, 6.0, "C"]
]
calculate_subarray_sums(inp)
