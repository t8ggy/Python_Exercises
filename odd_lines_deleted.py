file = open("C:\\Users\\Iain\\Documents\\QA\\Python\\filename.txt", "r")

outfile = ""

for line in range(1, 11):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline()

file = open("C:\\Users\\Iain\\Documents\\QA\\Python\\filename.txt", "w")
file.write(outfile)
file.close()