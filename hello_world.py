# print("Hello World")
# home='My family house'
# work='My office'
# print("home")
# print("work")

# home='My current house'
# home =='My Current house'
# print(home, "and", work)

# #constant to be written in capital

# AGE = 12


# my_string = 'Some randome String'
# print(my_string)

# print(my_string[6])


# #for item in my_string:
# #    action = 'ran'
#  #   if item in action:
#  #       print(item)



# #for item in my_string:
#  #   action = 'ran'
#   #  if item in my_string:
#    #     print('yes')     



# action = 'ran'
# if action in my_string:
#     print('yes')             



# print(len(my_string))

# #interger/int, float

# my_int = 123456789
# print(type(my_int))
# my_long_int= 123456960694939399329393948484848823882183821838138838482484832848484
# print(type(my_long_int))
# my_float=1234.567
# print(type(my_float))

# #Arithmetics logical, comparison, 
# my_first_var=2
# my_sec_var=3
# print(my_first_var + my_sec_var)
# print(my_first_var - my_sec_var)
# print(my_first_var / my_sec_var)
# print(my_first_var * my_sec_var)
# print(my_first_var % my_sec_var)
# print(my_first_var ** my_sec_var)
# print(my_first_var // my_sec_var)

# print(2>3)

# x=1.1 + 2.2
# print(x)

# #logical comparison: And, Or, false and false=false, false and true=true

# print(my_first_var==my_sec_var)
# print(my_first_var>my_sec_var)
# print(my_first_var<my_sec_var)


# # identity operators is/ is not

# my_string_1="boy"
# my_string_2="girl"
# my_string_3="boy"

# print (my_string_1 == my_string_3)

# #bitwise operators if an only if if both operands are 1 for &, OR operator returns 1 if atleast one operand is 1

# a=10
# b=4
# bin(a)
# print(bin(a))
# bin(a&b)
# print(bin(a&b))
# bin(a|b)
# print(bin(a|b))
# c=300
# print(bin(~300 & 255))
# bin(c)
# print(bin(c))

# d=840
# print(bin(~840 & 255))

# bin(d)
# print(bin(d))


# print('e')


# f= 1152
# bin(f)
# print(bin(f))

# print(bin(~1152 & 1023))


# g=10
# h=4
# bin(g<<h)
# print(bin(g<<h))

# 2 + 10 * 5

# print(2 + 10 * 5)

# # List, updating a list and all about a list. . Its a collectn of ojst, separated with commas.

# Fruits = ['orange','pple','nana']

# print(Fruits)

# my_list = [1,2,3,4]
# my_list2 =[2,"john", 4.5, [6,"boy"]]

# print(my_list2)
# print(type(my_list))

# print(my_list2[3])
# print(my_list2[3][1])

# my_list3 = [1,2,3,4,5,6,7,8,9,'a', 'b', 'c', 'd', 'e','f']
# print(my_list3[-6])#from the back at index 5
# print(my_list3[0:9]) #everything from 0-index 8
# print(my_list3[-6:-1])
# #logic is my_list3[start: end]

# # append

# my_list3.append('g') #adding a single item
# print(my_list3)

# my_list3.extend(['h','i','j']) #to add multiple items
# print(my_list3)

# #To concat two list

# odd_list=[1,3,5]
# even_list=[2,4,6]
# odd_list + even_list
# print(odd_list + even_list)

# my_list3[-3:] # to get the last 3
# print(my_list3[-3:])

# sub_my_list3 = my_list3[-3:]
# print(sub_my_list3)
# sub_my_list3 * 3
# print(sub_my_list3 * 3)

# my_list3.insert(9,0)
# print(my_list3.insert(9,0))
# print(my_list3)

# del my_list3[9]
# print(my_list3)

# del my_list3[-10:]
# print(my_list3)
# my_list3.remove(9) #removes the item specified

# print(my_list3)

# my_list3.pop(7) # RETURNSs the value of the item that will; be removed

# print(my_list3)

# my_list3.pop() # returns the value of the item to be removed which is the last item in the list.
# print(my_list3)
# my_list3[-1] = "j"
# print(my_list3)

# my_list2.clear() #clears everything in the list
# print(my_list2)

#List conprehension



# my_list3 = [1,2,3,4,5,6,7,8,9,'a', 'b', 'c', 'd', 'e','f']

# my_list_comp = [x for x in my_list3 if type(x) is int]
# print(my_list_comp)

# print(0 in my_list_comp)

# print(9 in my_list_comp)


#TUPLES; very similar to list but are not mutable. They start with ()

my_tuple = (1,2,3,4)
my_tuple2 = (2, "John", 4.5, [4,"boy"], ("Some", "tuple"))

print(type(my_tuple))
print(type(my_tuple2))

my_tuple3 = 1, 2, "big", "bold"

print(type(my_tuple3))

#unpack  a tuple
d,e,f,g = my_tuple3
print(d)
print(g)

# another case, some element equals tuples

#some_tuple =(some_element) #error because some_element is not in quote

some_tuple =("some_element") # correct but python sees it as a string

some_tuple =("some_element",) # correct but python sees it as a tuple because it has a comma after it indicating it is a collection of an item

# we can access the items in a tuple by referencing the index

print((my_tuple))
print(my_tuple)
print(my_tuple[2])

print(my_tuple2[1])
print(my_tuple2[3][1])
print(my_tuple2[1:4])

#note that items in a tuple are not mutable but a list in a tuple can be changed. see example below

my_tuple2[3][1] ="girl"
print(my_tuple2)


my_sub_tuple = my_tuple2[-1]

print(my_sub_tuple)

my_sub_tuple *3
print(my_sub_tuple *3)

#since it cant be changed, we can delete from py memory

# del my_sub_tuple
# print(my_sub_tuple)

#COUNT and INDEX are the only two methods to work wt in a TUPLE. count can be used to count the no of occurence of an item in a tuple #Index is used to get the index of an item in a tuple.
my_new_tuple =('m','y','l','e','t','t','e','r')
print(my_new_tuple)
print(my_new_tuple.count('t'))
print(my_new_tuple.index('y'))

## When is it ideal to use a tuple? WHEN SPEED IS IMPORTANT! 2) WHEn u need to consider the index of items.


# to convert a list to a tuple
my_listo = [1,2,3,4]
my_tupleE = tuple(my_listo)
print(my_tupleE)
print(type(my_tupleE))

##SETs in python. every element(items) of a set must be mutable/changeable 


my_set ={1,2,3,4}

my_empty_set = set()

print(type(my_set))

print(type(my_empty_set))

#my_set2 = {1,2,"Johnny", ["some", 4.5]} #error because its a misture of mutable and not mutable

my_set2 = {1,2,"Johnny", ("some", 4.5)} 
my_set3 = set(["some", 4.5])

print(my_set2)
print(my_set3)
my_set4 = {4,5,6,7}


#union
print(my_set.union(my_set4)) #or my_set | my_set4

#Intersection

print(my_set.intersection(my_set4)) #or my_set & my_set4

#difference of a set
print(my_set.difference(my_set4)) #0r my_set - my_set4
print(my_set4.difference(my_set)) #0r my_set4 - my_set
print(my_set ^ my_set4) # symmetric difference


####DICTIONARIES

my_dict = {
    "boy": "James",
    "Girl": "Joy"
}

my_dict2 = {
    "city": "Los Angeles",
    "Country": "USA"
}

print(my_dict)
print(my_dict2)

#using the keyvalue index to the the value
print(my_dict["boy"])

#using .get to extract the value of the key value
print(my_dict2.get("Country"))

#adding a new item into a dict
my_dict2["Continent"] = "North America"

print(my_dict2)

#replacing a value in the dict
my_dict2["city"] ="New York"
print(my_dict2)

#removing an item from a dict

my_dict.popitem() # this removes the last item

print(my_dict)

#To remove an item by specifying the keyValue of what you want to remove.
my_dict2.pop("Country")

print(my_dict2)

my_dict.clear()
print(my_dict)


#Dictionary conprehension

my_dict3 = {
    "number": [1,2,3,4],
    "strings" : "This is a string",
    "floats" :4.5,
}

print(my_dict3)


my_list_dict = {k:v for (k,v) in my_dict3.items() if type(v) is list}

print(my_list_dict)


#FLOW CONTROL If else

a=5
b=10
if b>a:
    print ("b is greater than a")

if a>b:
    print("a greater than b")
else:
    print("b is greater than a")





c=10
if c>20:
    print("c is greater than 20")
elif c<5:
    print("c is less than 5")
else:
    print(f"{c} is neither greater than 20 nor less than 5")        



#FOR LOOP

names =["James", "John", "Faustina"]
for name in names:
    if name.startswith("J"):
        print(name)




list_numb = [1,2,3,4,5,6,7,8,9]
for item in list_numb:
    if item % 2==1:
        print(item)


# num = input("Enter Number:")
# number = int(num)
# condition = 0
# count = 2
# iteration = 0

# while iteration <= number/2:
#     if number % count==0:
#         condition = 1
#         break
#     iteration += 1

# if condition ==0:
#     print(f"{number} is a prime number")
# else:
#     print(f"{number} is not a print number")


# namess =["James", "Joseph","john", "Peter","james","john"]
# unique = set()
# for name in namess:
#     if name.islower():
#         unique.add(name)
#         continue
#     unique.add(name.lower())
# print(unique)    


#FUNCTIONS

def my_func():
    print("This is my first fucntion")

my_func()

def check_prime_number(num):
    number = int(num)
    condition = 0
    count = 2
    iteration = 0

    while iteration <= number/2:
        if number % count==0:
            condition = 1
            break
        iteration += 1

    if condition ==0:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a print number")



check_prime_number(35)
check_prime_number(19)
check_prime_number(20)
check_prime_number(37)


### another example

# def add_num(num1, num2, num3):#when you specify the number of args
#     final_num = num1 + num2 + num3
#     return final_num


# ## If we dont need to specifi=y the number of argument to be expected

# # def add_num(*nums):
# #     final_num = 0
# #     #print(f" Type of argument is: {type(num)}")
# #     for num in nums:
# #         final_num += num
# #     return final_num    


# # print(add_num(1,2,3,4,5,6,7,8,9))


# print(add_num(1,2,3))


##postional and keyword argument


def calc_num(num1,**kwargs):
    print(f"type of argument is : {type(kwargs)}")
    num2 =kwargs.get("num2")
    num3 =kwargs.get("num3")
    final_num = 0

    for k,v in kwargs.items():
        final_num += v
    return final_num    
    






















