a=2
b=3
num_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


for i in num_list:
    if i % a == 0 and i % b == 0:
        print("True")
    else:
        print("False")