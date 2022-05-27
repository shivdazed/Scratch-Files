""""
feb9th2022
var1 = 100
var2 = 50

if var1 < var2:
    print("Var1 is less than var2")
else:
    print("Var1 is greater than var2")
"""
"""
var = int(input("Enter a number to check if positive or negative:"))

if var >0:
    print("Number inputted is Positive")
else:
    print("Number is Either zero or negative.")
"""
"""
i = input("Enter an alphabet:")

if i =='a' or i =='e' or i=='i' or i =='o' or i =='u':
    print("Entered alphabet is a Vowel")
else:
    print("Entered alpabet is a consanant and not a vowel")
"""

"""
var = int(input("Enter a number:"))

if var >= 0:
    if var==0:
        print("Given number is zero")
    else:
        print("Given number is positive")
else:
    print("Given number is negative")


"""

#for- finite iteration
#while - infintie iterations
"""
#for
var1 = "45781"
for i in var1:
    print(i)

num = 50
for i in range(0,num+1,7):
    print(i)



n = 100
#evennumbers
#for e in range(0,n+1,2):
#        print(e)

#oddnumbers
#for o in range(1,n+1,2):
#        print(o)

#tables of numbers
n = 27
for i in range(1,10+1):
    print(n,"x",i ,"=",(n*i))
"""

##Task --- take input from user, check if prime or not
##Task2 -- find reverse of given number
##Task3 --- Find if input is a twisted prime number or not(If prime palindrome )
"""
num = 56
i = 0
while(i<num):
    print(i)
    i = i+1
"""
##Feb 9th2022####
#
# ##task1prime or not
# n = int(input("Enter a number for prime check:"))
#
# if n>1:
#     for i in range(2,n):
#         if(n%i==0):
#             print(n,"Is not prime number")
#             break
#     else:
#         print(n,"is a prime number")
# else:
#    print(n,"is not a prime number")

##TASK 2 REVERSE A number
#
# n = int(input("Enter a number:"))
# r = int(str(n)[::-1])
# print("Reverse is:",r)


#task 3
#
# n = int(input("Enter a number for prime check:"))
# f = False
# if n > 1:
#     for i in range(2, n):
#         if (n % i == 0):
#             print(n, "Is not prime number")
#             break
#     else:
#         print(n, "is a prime number")
#         rev_n = int(+str(n)[::-1])
#         if rev_n == n:
#             if rev_n > 1:
#                 for j in range(2, rev_n):
#                     if (rev_n % j == 0):
#                         print(rev_n, "Is a Skewed Prime number")
#                         break
#                 else:
#                     print(n, " not skewed  prime number")
# else:
#     f = False
#
#
# if r>1:
#     for j in range(2,r):
#         if(r%j==0):
#             print(r,"Is not a reverse prime number")
#             break
#
#     else:
#         print(r,"is a reverse prime number")
# else:
#    print(r,"is not a reverse prime number")
##HW
##Task1-- Program to find out factorial of 9 using for loop
###Task2 --- program to find multiplication table
#####BREAK AND CONTINUE STATEMENTS

# ##break
# for i in range(0,1000):
#     if i == 100:
#         break
#     else:
#         print(i,"\n")
#
# ##continue
#
# for i in range(0,100):
#     if i%3==0:
#         continue
#     print(i)
#

##task--- program to find out reverse of a number 12345
##task--- program to find sum of all num inside a list
##task--- print string data except 'i' and the given data is "hi friends welcome to livewire " using continue statement

##14th Feb 2022

# list methods---definition is []
# mylist = [1,2,3,4,5,6,7]
# print(mylist)
# print(type(mylist))
#
# print(mylist[3])
# print(mylist[-1])
# print(mylist[0:3:2])
#
# mylist[3]= 7
# print(mylist)
#
# print("Size of my list:",len(mylist))
#
# mylist.append(10)
# print(mylist)
#
# mylist.append([11,22,33])
# print(mylist)
#
# print(mylist.pop())
# print(mylist)
# #pop by default takes -1 index postion as argument and cannot take a data element as argument
# print(mylist.pop(4))
# print(mylist)
#
# print(mylist.remove(10))
# print(mylist)
#empties existing list created
# print(mylist.clear())
# print(mylist)
#permanently destroys created data structure
# del mylist

##string  str--- ' ' "" ''' ''' """ """
#string is immutable cannot be modified once created, it can be deleted
# mystr = "Hii Anuroop "
# print(mystr)
# print(type(mystr))
# print(mystr[4])
# print(mystr[:3])
# print(mystr[4:])
# print(mystr[-4])
# print(mystr[-7:])
#
# #methods
# print(mystr.lower())
#
# print(mystr.upper())
#
# print(mystr.capitalize())
#
# print(mystr.count("n"))
#
# print(mystr.index("n"))
#
# del mystr


###dictionary 21st Feb 2022
# #syntax
# #dic = {key:Values}
#
# info ={ "name":"Anuroop",
#         "mob_no.": 9820448729,
#         "location": "Thane",
#         "address" : "Lokpuram,Vasant Vihar"
# }
#
# print(info)
# print(info["mob_no."])
# print(info["address"])
#
# infolis ={ "name":["Anuroop","Vishak","Vishakha","Pratik"],
#         "mob_no.": [9820448729,9797070232,9869860643,9698644424],
#         "location": ["Thane","Lower Parel","Goregaon","Malad"],
#         "address" : ["Lokpuram,Vasant Vihar","Aarey Colony","Near Railway Station","Opposite Oberoi Mall"]
# }
# print(infolis)
# print(infolis["mob_no."][3])
# print(infolis["name"][-1])
# print(infolis["address"][-1])
b = [11,33,22]
infolisnested ={ "name":["Anuroop","Vishak","Vishakha","Pratik"],
        "mob_no.": [9820448729,9797070232,9869860643,9698644424,[2225883843,2227785748,2227846483]],
        "location": ["Thane","Lower Parel","Goregaon","Malad"],
        "address" : ["Lokpuram,Vasant Vihar","Aarey Colony",["Vartak Nagar","Shivai Nagar","Shastri Nagar"],"Near Railway Station","Opposite Oberoi Mall"]
}
# print(infolisnested["mob_no."][-1])
# print(infolisnested["address"][2])
# print(infolisnested["mob_no."][4][0])
# print(infolisnested["address"][2][-1])
#
# for i in infolisnested.items():
#     print(i)
#
# for j in infolisnested.values():
#     print(j[1])
#
# for k in infolisnested.keys():
# #     print(k)
#
# infolisnested.update({"name":"Omkar"})
# print(infolisnested["name"])
#
# g = infolisnested.get("location")
# print(g)

#student nested dictionary, minimum 3 students, name subject and marks, City use the appropriate datastructures
#task 2 try with employee details

student ={
            "student1": {"Name":("Anuroop","Shivdasan"),
                         "Subject":["Maths","Philsophy","History"],
                         "Marks":[90,79,80],
                         "City":("Thane",),
                         },
            "student2":{"Name":("Laukik","Kambli"),
                         "Subject":["History","Maths","Philosophy"],
                         "Marks":[99,66,99],
                         "City":("Panjim",),
                         },
            "student3": {"Name": ("Abhishek","Sarang"),
                 "Subject": ["Philosphy","History","Maths"],
                 "Marks": [100,78,87],
                 "City":("Navi Mumbai",),
                 },

}

print("Name:",student["student3"]["Name"])
print("Subject:",student["student3"]["Subject"])
print("Marks in each respective:",student["student3"]["Marks"])
print("City:",student["student3"]["City"])

print(student["student1"]["Subject"])
student["student1"]["Subject"].clear()
student["student1"]["Subject"].extend(["Physics","Chemistry","Biology"])
print(student["student1"]["Subject"])

employee ={
            "Chinese": {"Index of Item":[1,2,3,4,5,6,7,8,9,10],
                         "Dish_Name":["Manchow Soup","Chicken Crispy","Chicken Chilli","Chicken Triple Rice","Chicken Triple Noodles","Chicken Schezuan Fried Rice","Chicken Schezuan Niidels","","",""],
                         "Type of Dish":["Soups","Appetizers","Rice","Noodles","Main Course","Deserts","Extra Sides","Soft Drinks and More"],
                         "Price":("","","","","","","","","",""),
                         },
            "South Indian":{"Name":("Laukik","Kambli"),
                         "Subject":["History","Maths","Philosophy"],
                         "Marks":[99,66,99],
                         "City":("Panjim",),
                         },
            "": {"Name": ("Abhishek","Sarang"),
                 "Subject": ["Philosphy","History","Maths"],
                 "Marks": [100,78,87],
                 "City":("Navi Mumbai",),
                 },

}
