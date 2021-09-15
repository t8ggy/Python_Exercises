i = 0
 
string2 = "aBC-d34g"
list = []
 
if len(string2) % 2 == 0:
    while i in range(0,len(string2)):
        ascii = ord(string2[i])
        if ascii in range(97,123):
            ascii -= 32
        else:
            blank = 1
 
        letter = chr(ascii)
        list.append(letter)
        i += 1
else:
    while i in range(0,len(string2)):
        ascii = ord(string2[i])
        if ascii in range(65,91):
            ascii += 32
        else:
            blank = 1
 
        letter = chr(ascii)
        list.append(letter)
        i += 1
 
output_string = ""
for ele in list:
    output_string += ele
 
print(output_string)