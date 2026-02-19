import numpy as np

# Why range and slicing don't include the last element -
my_list = [1, 3, 3, 6 , 3]
print(my_list[:3]) # easy to interpret the length of the number of items produced by slicing
print(my_list[3:]) # total len - 3 = 2

# start:step:stop -
print(my_list[::3]) # start: omitted, stop: omitted, step = 3
print(my_list[::-3]) # 3 steps in reverse
print(my_list[:1:-1]) # stop at index 1

# Multidimensional slicing
a = np.array([[1, 2, 3, 10, 11, 15], [4, 5, 6, 12, 14, 20]])
print(a[1, 2]) # Gets element at position (1, 2)

print(a[0:2, 0:2]) # two-dimensional slice, first 2 elements of both arrays


# ellipsis (...) -
x = np.array([[[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[11, 22, 33], [44, 55, 66], [77, 88, 99]]],
              [[[111, 222, 333], [444, 555, 666], [777, 888, 999]], [[1111, 2222, 3333], [4444, 5555, 6666], [7777, 8888, 9999]]]])

print("\n")
print("x[0]: ", x[0]) # first array in outermost block
print("\n")
print("x[1]: ", (x[1])) # second array in outermost block

print("\n")
print(x[1, ...])
'''
This is a 4D array of shape (2, 2, 3, 3)
first axis = 0th index (2)
second axis = 1st index (2)
third axis = 2nd index (3)
fourth axis = 3rd index (3)
x[1, ...] = x[1, :, :, :] = x[1] OR select second element along axis 0
along sub axes fill everything
select everything along first axis
'''

# pick the 3rd pixel in the third channel of the second image in 1st batch
pixel = (x[0][1][2][2])
print("Pixel value: ", pixel)


# slices change mutable sequences in place
my_list[2:4] = [10, 9]
print(my_list)

del my_list[:2]
print(my_list)

my_list[:2] = [10]
print(my_list)