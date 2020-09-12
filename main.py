# a list is a sequence of items 
# 1D list like a single row or a single column in Excel
# Declare a list using [] and a coma seperated of values

list_ints = [0, 1, 10, 20]
#there are unique indexes for each element in the list
# 0-based, meaning the first element is at zero and the last element is n-1
# where n is the number of elements in this list 
# 0 (0), 1 (1), 10 (2), 20(3)
print(list_ints[0])
print(list_ints[-4])

#types can be mixed in a list
list_numbers = [0, 0.0, 1, 1.0, -2]
print(list_numbers)
print(type(list_numbers))
#lists are mutable 
list_numbers[0] = "hello"
print(list_numbers)

# ise len() to figure out how many elements are in a list
print(len(list_numbers))
list_numbers.append("another element")
# print out the last element in the list when you dont knoe the number of elements in the list
print(list_numbers[len(list_numbers)-1])

# we can have an empty list 
empty_list = []

# we can have lists of lists
nested_list = [[0,1], [2], [3], [4, 5]]
print(len(nested_list))
print(len(nested_list[0]))

# looping through list items
candies = ["twix", "sneakers", "smarties"]
print(candies)

for candy in candies: 
    print(candy)

i = 0
while i < len(candies): 
    print(i, candies[i])
    i += 1

i = 0
for i in range(len(candies)): 
    print(i, candies[i])

# common list operators
# list concatenation.. adding two lists together
print(candies)
candies += ["m&ms", "starburst"]
print(candies) 
# list repitition... repeating elements in a list
bag_o_candies = 5 * ["twix", "snikers"]
print(bag_o_candies) 
#list sclicing 
print(candies[1:3]) # : is the slice operator. start index is inclusive 
#end index is exclusive
# if you ever need a copy of a list you can simply use the : with no start or end
copy_of_candies = candies[:]
copy_of_candies[0] = "TWIX"
print(copy_of_candies)
print(candies)

#list methods candies.
