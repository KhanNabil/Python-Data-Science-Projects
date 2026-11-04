students = []

for i in range(5):
    while True:
        student = int(input("Enter marks: "))
        if student >= 0 and student <= 100:
            students.append(student)
            break
        else:
            print("Invalid Marks")

total = sum(students)
perc = total/500*100

print("Total marks:",total)
print("Percentage:",perc)


if total >= 450:
    grade = "A"
elif total >= 350:
    grade = "B"
elif total >= 250:
    grade = "C"
elif total >= 150:
    grade = "D"
else:
    grade = "Fail"
print("Grade:",grade)


