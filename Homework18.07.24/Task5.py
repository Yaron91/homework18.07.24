import random
#a.
num_list = [random.randint (0 , 9999) for i in range (4)]
print ("a.", num_list)
#b.
num_user: list = []
while True:
    x = int (input ("Please enter a number, to exit type -999: "))
    if x == -999:
        break
    else:
        num_user.append(x)
print (num_user)