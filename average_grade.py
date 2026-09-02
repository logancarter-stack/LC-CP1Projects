
while True:
    try:
        one=int(input("what is your grade for first period:"))
    except:
        print("thats not a number")    
    else:
        break

while True:
    try:
        two=int(input("what is your grade for second period:"))
    except:
        print("thats not a number")    
    else:
        break

while True:
    try:
        three=int(input("what is your grade for third period:"))
    except:
        print("thats not a number")    
    else:
        break
while True:
    try:
        four=int(input("what is your grade for fourth period:"))
    except:
        print("thats not a number")    
    else:
        break
while True:
    try:
        five=int(input("what is your grade for fifth period:"))
    except:
        print("thats not a number")    
    else:
        break
while True:
    try:
        six=int(input("what is your grade for sixth period:"))
    except:
        print("thats not a number")    
    else:
        break

while True:
    try:
        seven=int(input("what is your grade for seventh period:"))
    except:     
        print("thats not a number")    
    else:
        break
total_num=one+two+three+four+five+six+seven
average_grade=(total_num/7)
print(average_grade) 
print('yay')