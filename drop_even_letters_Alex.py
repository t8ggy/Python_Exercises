input_string = input("Please input your string of characters: ")
string = input_string.lower()
output_list = []
output_string = ""
 
for i in range (0,len(string)):
    ascii = ord(string[i])
    if ascii in range(97,123) and ascii % 2 == 0:
        letter = chr(ascii)
        output_list.append(letter)
    i +=1
 
for ele in output_list:
    output_string += ele
 
print(output_string)