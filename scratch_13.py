#print("Hello")

# Your last Python code is saved below:
# print "Hello"
# #Q1. Join items of given list using "and" and print the string
# #weekdays = ['sun','mon','tue','wed','thu','fri','sat']
#    #Output:  'sun and mon and tue and ....'
# def convertToString(weekdays):
#     #Write your code here


# #Q2. count the occurrences of a particular element in the list and
# #   output highest occurring element
# 	# Output: Mon (Since monday occurred 3 times)
# days=['sun','mon','tue','thu','fri','sun','mon','mon']
# def findMaxOccuringString(days):
days = ['sun', 'mon', 'tue', 'thu', 'fri', 'sun', 'mon', 'mon']
r = []
for i in range(len(days)):
    c = days.count(days[i])
    r.append(c)
print(r)
count_max_ele= max(r)
for m in days:
    if days.count(m) == count_max_ele:
        print("Element with maximum reps-",m)
# #Q3. Write a function to print the following pattern on the #screen.

# *****
# ****
# ***
# **
# *

# #The height of this pattern will be taken as input

# def designPattern(height):
"""for i in range(2):
  #print("*")
  for j in range(1):
    print("*\n",end = '')
"""

# #Q4. Write a program to convert the first character of each #word in a sentence to uppercase.
# #For ex -
# #Inp: this is a test sentence.
# #Out: This Is A Test Sentence.

# def modifyString(sentence):
# 	#Write your code here


# #Q5. Write a program to check whether a given substring is #present in the string or not.
# #Main string: thisisateststring
# #Substring: test


# #Output: True

# def isSubStringPresent(sub_str, main_str):
# 	#Write your code here


# Q6. Implement the unique_names method. When passed two lists of names, it will return a list containing the names that appear in either or both lists. The returned list should have no duplicates.

# For example, calling unique_names(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma']) should return a list containing Ava, Emma, Olivia, and Sophia in any order.


# def unique_names(names1, names2):
#     return None

# if __name__ == "__main__":
#     names1 = ["Ava", "Emma", "Olivia"]
#     names2 = ["Olivia", "Sophia", "Emma"]
#     print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia


# Q7. Implement a group_by_owners function that:
# Accepts a dictionary containing the file owner name for each file name.
# Returns a dictionary containing a list of file names for each owner name, in any order.
# For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.

# def group_by_owners(files):
#     return None

# if __name__ == "__main__":
#     files = {
#         'Input.txt': 'Randy',
#         'Code.py': 'Stan',
#         'Output.txt': 'Randy'
#     }
#     print(group_by_owners(files))


# Q8. Write a program to get all prime numbers between a given range.
# def printPrimes(start, end):
# 	#Write your code here




