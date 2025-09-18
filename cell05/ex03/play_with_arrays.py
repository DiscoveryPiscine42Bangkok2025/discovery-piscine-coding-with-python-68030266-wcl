array = [2,8,9,48,8,22,-12,2]

print(array)

result = [X + 2 for X in array if X > 5]
result = set (result)
print (result)