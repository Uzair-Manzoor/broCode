# sort () method = used with lists
# sort () function = used with iterables

students = ["Murtaza","Atif","Orhan","Nasir","Rahim","Kazim","Muhammad Ali","Haider Abbas", "Perveen"]

#students.sort()
#students.sort(reverse=True)
#students.sort(key=True)

sorted_students = sorted(students,reverse=True)

#students.append("Zafar")

for i in sorted_students:
    print(i)

#______________________________________________________________
# Level 2


students = [("Atif", "F", 60),
            ("Murtaza","A", 33),
            ("Orhan","D", 36),
            ("Paeveen","B", 20),
            ("Mr. Nasir","C", 78)]

#grade = lambda grades:grades[1]
age = lambda ages:ages[2]
students.sort(key=age)
#students.sort(key=age,reverse=True)

for i in students:
    print(i)

#___________________________________________________

students = (("Atif", "F", 60),
            ("Murtaza","A", 33),
            ("Orhan","D", 36),
            ("Paeveen","B", 20),
            ("Mr. Nasir","C", 78))

sorted_students = sorted(students,key=age)

for i in sorted_students:
    print(i)