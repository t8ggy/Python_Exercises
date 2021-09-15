name = str(input("Enter your name: "))
homework = int(input("Enter your homework score: "))
assessment = int(input("Enter your assessment score: "))
exam = int(input("Enter your exam score: "))

def add_calc(number1, number2, number3, number4):
    answer= (number1+number2+number3)/number4*100
    return answer

Final_Grade= add_calc (homework, assessment, exam, 175)
print("Hello ", name, "your final score is ", Final_Grade,"%")
