def deep_reverse(lst):
    result = []
    for item in reversed(lst):      
        if isinstance(item, list):  
            result.append(deep_reverse(item))
        else:
            result.append(item)
    return result



input_data = [[1, 2], [3, 4], [5, 6, 7]]
output = deep_reverse(input_data)

print(output)
