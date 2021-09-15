a_fruit="Banana"
a_greengrocer=["apple", "pear", "banana", "Kiwi", "strawberry"]

fruit=a_fruit.lower()
greengrocer=[x.lower() for x in a_greengrocer]

place=greengrocer.index(fruit)

last_fruit = greengrocer[-1]
if place==0:
    print(greengrocer[1])
elif fruit==last_fruit:
    print(greengrocer [place -1])
else: 
    print(greengrocer[place -1])
    print(greengrocer[place +1])