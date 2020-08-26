# for number in range (0,101,2):
#   print(number)

# number = 0
# while number < 101:
#   if not number%2:
#        print (number)
#   number +=1

# for item in range (101):
#     if item % 2 == 0:
#         continue
#     print(item)

# number = 0
# while number < 101:
#   if number%2:
#        print (number)
#   number +=1

# my_list = [*range(101)] 
# print(my_list) 

# for item in my_list:
#     if not item%2:
#         print("This list contains odd numbers")
#         break

my_list = [*range(200)] 

for item in my_list:
    my_list[item]=float(my_list[item])
print (my_list)