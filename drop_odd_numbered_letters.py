string_x = "Mathematical"
i=0

if len(string_x) > 0:
    while i in range(0,len(string_x)):
      if ord(string_x[i]) % 2 == 1:
        print(i)
        i += 1

else:
    print("nothing")

#if ascii % 2 !=0: