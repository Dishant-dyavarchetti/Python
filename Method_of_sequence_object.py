# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

mylist = [10,20,30,40]
print(type(mylist))

print(mylist[0])
print(mylist[2])
print("\n")
print(mylist[-1])
print(mylist[-2])


#slice
mylist2 = [10,20,30,40,50]

print(mylist2[1:4])
print(mylist2[2:])
print(mylist[:3])

print("\n")
print(mylist2[-5::2])
print(mylist2[-1::-1])
print(mylist2[-5::])

#modifying list
mylist[0] = 5
print(mylist)

#list Comprehension
number = [1,2,3,4,5]
squared_number = [x**2 for x in number]
print(squared_number)

#nested list
matrix = [[123],[4,5,6],[7,8,9]]
print(matrix[1][2])

#list operations
#length

length = len(mylist)
print(length)

#count
mylist2.append(50)
count = mylist2.count(50)
print(count)

#index
print(mylist.index(20))

#reverse
mylist.reverse()
print(mylist)

#sort
mylist2.sort()
print(mylist2)

#append
mylist.append(69)
print(mylist)

#insert
print(mylist2)
mylist2.insert(3, 35)
print(mylist2)

#extend
l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
print(l1)

#remove
print(l1)
l1.remove(6)
print(l1)

#Clear
l1.clear()
print(l1)

#pop
print(mylist)
mylist.pop();

print(mylist)

#copy
print(mylist2)
mylist = mylist2.copy()
print(mylist)

#cloning
l3 = l2[:]
print(l3)