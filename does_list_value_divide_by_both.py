a=2
b=3
num_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for i in num_list:
    if i % a == 0:
        c="true"
else:
    c="false"

if i % b == 0:
        d="true"
else:
    d="false"

if c=="true" and d=="true":
    print("true")
else:
    print("false")
