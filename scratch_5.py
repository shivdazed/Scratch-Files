fruits = [l for l in input("Enter fruits:").split()]

text = 'Hello python programmer'
#starts from 0 upto 6th position
print(text[0:7])

#default start from beginning to 6th position
print(text[:7])

#start from 4th and default printing till end
print(text[4:])

#default start to finish operator
print(text[::])

#default start to end with a step count of 3
print(text[::3])

#inserts at 0th indice
fruits[0:0] = 'yo'
print(fruits)

#inserts yolo before yo
fruits[:0] = 'yolo'
print(fruits)

#slices out list and keeps b at start
fruits[0:] = 'b'
print(fruits)

