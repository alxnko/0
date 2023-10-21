# array = [1, 2, 3, 4, 5]
array = ["a", "b", "c"]
# print("".join(array))
string = "12345"
# взять строку с 0 до 2 (не включительно) символов, добавить 1 и добавить с 3 символа
string = list(string)
string[2] = "1"
# соединяет элементы листа по разделителю ""
string = "-".join(string)
# print(string)

integer = 0
string = "0,1,2,3,4,5,6,7"
array = [int(i) for i in string.split(",")]
# price = [85, 748.57, "$"]
price = "85748.57$"
# print(string + str(integer))
array = ["Hello,", "University!"]
lens = []
array = [i.strip(",.!") for i in array]
for i in array:
    lens.append(len(i))
# print(array)
# print(lens)
newarray = []
# print(list(zip(array, lens)))
for i in range(len(array)):
    newarray.append(array[i])
    newarray.append(lens[i])
# print(newarray)
# for i in array:
#     print(i)
# for i, v in enumerate(array):
#     print(i, v)
# for word, ln in zip(array, lens):
#     print(word, ln)

# print(float(price.strip(",$ ")))

# DICTIONARY

# print(set("ahahahahaha"))
# print(set({1, 1, 2, 2, 3, 4}))
# nabor = {1, 2, 3, 4, 5, 6}
# nabor.add(1)
# nabor.add(1)
# print(nabor)
dictionary = {"key": [], "key": 2345}
# dictionary["key"] = 324234
print(dictionary)
