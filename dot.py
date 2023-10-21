# # string
# string = "1,2,3,4,5,6"
# print(string.strip(","))
# print(string.split(","))
# print(string.replace(",", "."))
# print(string.join(["AAAAAA", "BBBBBB", "CCCCCC"]))
# print(f"{100 - 199}, {[string]}")
# print("{}, {}".format(100 - 199, [string]))

# integer
# nothing

# array
array = [1, 2, 3, 4, 5, 6, 7]
array.append(7)
array.remove(7)
array.pop()
array.index(2)
array.reverse()
len(array)
enumerate(array)
zip(array, [1, 2, 3, 4, 5, 6])
print(array)

# set
set = {1, 2, 3, 4, 5, 6, 7}
set2 = {5, 6, 7, 8, 9}
# set.add(2)
# set.remove(2)
# set.pop()

# print(set - set2)
# print(set.difference(set2))
# # is this equal?
# print(set2 - set)
# print(set2.difference(set))

# print(set & set2)
# print(set.intersection(set2))

# print(set | set2)
# print(set.union(set2))

# string = "123456789"
# array = list(string)
# array.reverse()
# print("".join(array))

# dictionary

d = {"key": "value", "key2": "value"}

print(list(d.items()))
print(list(d.keys()))
print(list(d.values()))
print(d.get("key") == d["key"])
print(d.pop("key"))  # delete key and return value
print(list(d.items()))
