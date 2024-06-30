# Variable: A storage location identified by its name, containing some value.
# Question: Assign a value of 10 to variable a and 20 to variable b
# Question: Store the result of a + b in a variable c and print it. What is the result of a + b?

a = 10
b = 20
c = a + b

print(f"The result of a + b is {c}")

#o/p: The result of a + b is 30

l = [1, 2, 3, 4]

# Question: How do you access the elements in index 0 and 3? Print the results.
print("Element in index 0 is:", l[0])
print("Element in index 3 is:", l[3])

# O/P: Element in index 0 is: 1
# O/P: Element in index 3 is: 4

d = {'a': 1, 'b': 2}

# Question: How do you access the values associated with keys 'a' and 'b'?
print("Value associated with key 'a' is:", d['a'])
print("Value associated with key 'b' is:", d['b'])

# O/P: Value associated with key 'a' is: 1
# O/P: Value associated with key 'b' is: 2

my_set = set()
my_set.add(10)
my_set.add(10)
my_set.add(10)

# Question: What will be the output of my_set?
print("my_set is:", my_set)

# O/P: my_set is: {10}

my_tuple = (1, 'hello', 3.14)

# Question: What is the value of my_tuple?
print("my_tuple is:", my_tuple)

# O/P : my_tuple is: (1, 'hello', 3.14)


# Question: How do you access the elements in index 0 and 1 of my_tuple?
print("Element in index 0 is:", my_tuple[0])
print("Element in index 1 is:", my_tuple[1])

# O/P   Element in index 0 is: 1
# O/P   Element in index 1 is: hello

count_tuple = (1, 2, 3, 1, 1, 2)

# Question: How many times does the number 1 appear in count_tuple?
print("Number of times 1 appears in count_tuple is:", count_tuple.count(1))
 
 # O/P: Number of times 1 appears in count_tuple is: 3

 # Question: What is the index of the first occurrence of the number 2 in count_tuple?
print("Index of first occurrence of 2 is:", count_tuple.index(2))

#O/P: Index of first occurrence of 2 is: 1

# Question: How do you loop through a list and print its elements?
l = [1, 2, 3, 4]
for element in l:
    print(element, end=' ')

#O/P: 1 2 3 4


# Dictionary loop
# Question: How do you loop through a dictionary and print its keys and values?
d = {'a': 1, 'b': 2}
for key, value in d.items():
    print(f"Key: {key}, Value: {value}")

#O/P: Key: a, Value: 1
#O/P: Key: b, Value: 2

# Comprehension is a shorthand way of writing a loop
# Question: Multiply every element in list l with 2 and print the result
result = [element * 2 for element in l]
print("Result of multiplying every element in l with 2 is:", result)

#O/P: Result of multiplying every element in l with 2 is: [2, 4, 6, 8]


# Functions: A block of code that can be re-used as needed. This allows for us to have logic defined in one place, making it easy to maintain and use.
## For example, let's create a simple function that takes a list as an input and returns another list whose values are greater than 3

def gt_three(input_list):
    return [elt for elt in input_list if elt > 3]
## NOTE: we use list comprehension with filtering in the above function

list_1 = [1, 2, 3, 4, 5, 6]
# Question: How do you use the gt_three function to filter elements greater than 3 from list_1?
print("Elements greater than 3 in list_1 are:", gt_three(list_1))

#O/P: Elements greater than 3 in list_1 are: [4, 5, 6]

list_2 = [1, 2, 3, 1, 1, 1]
# Question: What will be the output of gt_three(list_2)?
print("Output of gt_three(list_2) is:", gt_three(list_2))

#O/P: Output of gt_three(list_2) is: []


#  Classes and Objects
# Think of a class as a blueprint and objects as things created based on that blueprint
# You can define classes in Python as shown below
class DataExtractor:

    def __init__(self, some_value):
        self.some_value = some_value

    def get_connection(self):
        # Some logic
        # some_value is accessible using self.some_value
        pass

    def close_connection(self):
        # Some logic
        # some_value is accessible using self.some_value
        pass

# Question: How do you create a DataExtractor object and print its some_value attribute?
data_extractor = DataExtractor(10)
print("some_value attribute of data_extractor is:", data_extractor.some_value)

#O/P: some_value attribute of data_extractor is: 10


# Question: How do you print the current date in the format 'YYYY MM DD'? (using strftime)
from datetime import datetime
current_date = datetime.now()
print("Current date is:", current_date.strftime('%Y %m %d'))

# O/P: Current date is: 2024 06 25

# For example, let's consider exception handling on accessing an element that is not present in a list l
l = [1, 2, 3, 4, 5]

# Question: How do you handle an IndexError when accessing an invalid index in a list?
try:
    print(l[46])
except IndexError as e:
    print("An IndexError occurred:", e)

# O/P: An IndexError occurred: list index out of range
