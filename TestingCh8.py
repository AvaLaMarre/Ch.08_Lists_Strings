"""
mylist = [2,3,5,6,8,9,10]
for i in range(len(mylist)):
    print(mylist[i]**2)
print(len(mylist))
print(mylist)

lists = [[1, 2], [3, 4], [5, 6]]

list = [2, 5, 8, 4, 9, 5, 4]
list[3] = 7
print(list)
for i in range(len(list)):
    if list[i] == 4:
        list[i] = 7
print(list)


print("hello", lists[2][0])
#mytuple = (2,3,5,6,8,9,10)

droids = ["C3PO", "R2D2", "BB8"]
numitems = len(droids)
print(numitems)
for i in range(len(droids)):
    print(droids[i])
for item in droids:
    print(item)


uhs_slogan = "My school is the best"
print(len(uhs_slogan))

print(uhs_slogan[-1])
print(uhs_slogan[:16])
print(uhs_slogan[13:])
print(uhs_slogan[-4:])
print(uhs_slogan[:13] + "awesome")

words = 1
for letter in uhs_slogan:
    print(ord(letter))
    if letter == " ":
        words += 1

print(words)
"""
num = 3000
print(f"There are {num:0<5d} things")