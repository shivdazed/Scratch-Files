my_info = {"name":"Anuroop",
           "age":"29",
           "city":"Thane",
           "Education":"B.E. in Computer Engineering",
            "Mobile No.":919820448729,
           }

print(my_info["name"])
print(my_info["age"])
print(my_info["city"])
print(my_info["Education"])
print(my_info["Mobile No."])


li_in={"name":["Anuroop","Anupama","Trisha","Kritisha","Nidhi","Suraj","Vikram","Vijay"],
       "age":[29,25,21,21,21,26,26,24],
       "city":["Thane","Toronto","New Delhi","Ahmedabad","Mulund","Bangalore","Queensland","Vikhroli"],
       "Education": ["B.E.","B.Biotech","l.L.B.","B.C.A.","B.Com","B.E.","M.Arch","B.C.A."],
       "Mobile No.": [9820448729,9142358625,9152862521,7728293221,7736289221,852424626,8823334264,8322234424],
       }
print(li_in)
print(li_in["name"][2])
print(li_in["age"][2])
print(li_in["city"][2])

li_in_nested={"name":["Anuroop","Anupama","Trisha","Kritisha","Nidhi","Suraj","Vikram","Vijay"],
       "age":[29,25,21,21,21,26,26,24],
       "city":["Thane","Toronto",["New Delhi","Thane"],["Ahmedabad","Thane"],"Mulund","Bangalore",["Queensland","Mulund"],"Vikhroli"],
       "Education": ["B.E.","B.Biotech","l.L.B.","B.C.A.","B.Com","B.E.","M.Arch","B.C.A."],
       "Mobile No.": [[9820448729,13145267275],9142358625,9152862521,7728293221,7736289221,852424626,8823334264,[8322234424,2225467484]],
       }
print(li_in_nested["name"][2])

print(li_in_nested["city"][2][1])

print("\nThe Whole Dictionary:")
for item in li_in_nested.items():
    print(item)

print("\nThe Dictionary Values:")
for item1 in li_in_nested.values():
    print(item1[1])
print("\nThe Dictionary Keys\:")
for item2 in li_in_nested.keys():
    print(item2)
print("\nUpdating The Dictionary Values for Key 'name'\:")
my_info.update({"name":"Pratham"})
print(["name"])

print("\nThe Dictionary Values for City\:")
g = li_in_nested.get("city")
print(g)
