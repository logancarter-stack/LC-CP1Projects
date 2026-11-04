#LC 1 letter grade 
'''A 94-100 
A- 90-93
B+ 87-89 
B 84-86
B- 80-82 
C+ 77-79
C 74-76 
C- 70-73
D+ 67-69 
D 64-66
D- 60-63 
F 0-59'''
grade = int(input("what is your grade: "))

if grade >= 94:
    print("You've got an A")
elif grade >= 90:
    print("You've got an A-")
elif grade >= 87:
    print("You've got an B+")
elif grade >= 84:
    print("You've got an B")
elif grade >= 80:
    print("You've got an B-")
elif grade >= 77:
    print("You've got an C+")
elif grade >= 74:
    print("You've got an C")
elif grade >= 70:
    print("You've got an C-")
elif grade >= 67:
    print("You've got an D+")
elif grade >= 64:
    print("You've got an D")
elif grade >= 60:
    print("You've got an D-")
else:
    print("You've got an F")