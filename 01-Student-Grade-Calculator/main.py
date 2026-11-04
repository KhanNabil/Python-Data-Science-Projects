students = []

n = 0

while True:
    n = int(input("Enter number of subjects: "))
    if n > 0:
        break
    else:
        print("Invalid Number of Subjects")



for i in range(n):
    while True:
        student = int(input("Enter marks: "))
        if student >= 0 and student <= 100:
            students.append(student)
            break
        else:
            print("Invalid Marks")

total = sum(students)
perc = round(total/(n*100)*100,2)

print("Total marks:",total)
print("Percentage:",perc)


if perc >= 90:
    grade = "A"
elif perc >= 70:
    grade = "B"
elif perc >= 50:
    grade = "C"
elif perc >= 30:
    grade = "D"
else:
    grade = "Fail"
print("Grade:",grade)

print("Highest marks:",max(students))
print("Lowest marks:",min(students))

gpa = (sum(students)/n)/10

print("GPA:",round(gpa,2))
