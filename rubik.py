
# lists of faces show top123, middle123 and bottom123 in that order for each face

frontf=[0, 0, 3, 0, 0, 3, 2, 2, 5]
downf=[5, 5, 0, 1, 1, 4, 1, 1, 4]
backf=[3, 5, 5, 0, 2, 2, 0, 2, 2]
leftf=[2, 2, 1, 3, 3, 1, 3, 3, 4]
upf=[4, 4, 1, 4, 4, 1, 2, 3, 3]
rightf=[4, 5, 5, 4, 5, 5, 1, 0, 0]

print("")
print("Start")
print(" ", "Front", "      ", "Down", "      ", "Back", "     ", "Left", "        ", "Up", "     ", "Right")
print(frontf[0:3], " ", downf[0:3], " ", backf[0:3], " ", leftf[0:3], " ", upf[0:3], " ", rightf[0:3])
print(frontf[3:6], " ", downf[3:6], " ", backf[3:6], " ", leftf[3:6], " ", upf[3:6], " ", rightf[3:6])
print(frontf[6:], " ", downf[6:], " ", backf[6:], " ", leftf[6:], " ", upf[6:], " ", rightf[6:])


# Front
for i in range(3):
        cube = []
        cube=frontf + downf + backf + leftf + upf + rightf
        order=(6, 3, 0, 7, 4, 1, 8, 5, 2, 45, 48, 51, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 9, 30, 31, 10, 33, 34, 11, 36, 37, 38, 39, 40, 41, 29, 32, 35, 42, 46, 47, 43, 49, 50, 44, 52, 53)
        turned_cube = []
        turned_cube = [cube[i] for i in order]
        frontf=turned_cube[0:9]
        downf=turned_cube[9:18]
        backf=turned_cube[18:27]
        leftf=turned_cube[27:36]
        upf=turned_cube[36:45]
        rightf=turned_cube[45:]

print("")
print("After F3")
print(" ", "Front", "      ", "Down", "      ", "Back", "     ", "Left", "        ", "Up", "     ", "Right")
print(frontf[0:3], " ", downf[0:3], " ", backf[0:3], " ", leftf[0:3], " ", upf[0:3], " ", rightf[0:3])
print(frontf[3:6], " ", downf[3:6], " ", backf[3:6], " ", leftf[3:6], " ", upf[3:6], " ", rightf[3:6])
print(frontf[6:], " ", downf[6:], " ", backf[6:], " ", leftf[6:], " ", upf[6:], " ", rightf[6:])

#right
for i in range(6):
        cube = []
        cube=frontf + downf + backf + leftf + upf + rightf
        order=(0, 1, 11, 3, 4, 14, 6, 7, 17, 9, 10, 18, 12, 13, 21, 15, 16, 24, 38, 19, 20, 41, 22, 23, 44, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 2, 39, 40, 5, 42, 43, 8, 51, 48, 45, 52, 49, 46, 53, 50, 47)
        turned_cube = []
        turned_cube = [cube[i] for i in order]
        frontf=turned_cube[0:9]
        downf=turned_cube[9:18]
        backf=turned_cube[18:27]
        leftf=turned_cube[27:36]
        upf=turned_cube[36:45]
        rightf=turned_cube[45:]

print("")
print("After R2")
print(" ", "Front", "      ", "Down", "      ", "Back", "     ", "Left", "        ", "Up", "     ", "Right")
print(frontf[0:3], " ", downf[0:3], " ", backf[0:3], " ", leftf[0:3], " ", upf[0:3], " ", rightf[0:3])
print(frontf[3:6], " ", downf[3:6], " ", backf[3:6], " ", leftf[3:6], " ", upf[3:6], " ", rightf[3:6])
print(frontf[6:], " ", downf[6:], " ", backf[6:], " ", leftf[6:], " ", upf[6:], " ", rightf[6:])      


#up
for i in range(1):
        cube = []
        cube = frontf + downf + backf + leftf + upf + rightf
        order=(45, 46, 47, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 27, 28, 29, 21, 22, 23, 24, 25, 26, 0, 1, 2, 30, 31, 32, 33, 34, 35, 42, 39, 36, 43, 40, 37, 44, 41, 38, 18, 19, 20, 48, 49, 50, 51, 52, 53)
        turned_cube = [cube[i] for i in order]
        frontf=turned_cube[0:9]
        downf=turned_cube[9:18]
        backf=turned_cube[18:27]
        leftf=turned_cube[27:36]
        upf=turned_cube[36:45]
        rightf=turned_cube[45:]

print("")
print("After U1 - final")
print(" ", "Front", "      ", "Down", "      ", "Back", "     ", "Left", "        ", "Up", "     ", "Right")
print(frontf[0:3], " ", downf[0:3], " ", backf[0:3], " ", leftf[0:3], " ", upf[0:3], " ", rightf[0:3])
print(frontf[3:6], " ", downf[3:6], " ", backf[3:6], " ", leftf[3:6], " ", upf[3:6], " ", rightf[3:6])
print(frontf[6:], " ", downf[6:], " ", backf[6:], " ", leftf[6:], " ", upf[6:], " ", rightf[6:])
print("")
#print(frontf)
#print(downf)
#print(backf)
#print(leftf)
#print(upf)
#print(rightf)

