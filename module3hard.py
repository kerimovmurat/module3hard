def calculate_structure_sum(data):
    total_sum = 0
    if isinstance(data, (int, float)):
            total_sum += data
    elif isinstance(data, str):
            total_sum += len(data)
    elif isinstance(data, (list, tuple, set)):
        for k in data:
            total_sum += calculate_structure_sum(k)
    elif isinstance(data, dict):
        for i, j in data.items():
            total_sum += calculate_structure_sum(j)
            total_sum += calculate_structure_sum(i)
    return total_sum
data = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data)
print(result)