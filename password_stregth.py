#lc password stregth 1
password = input("Enter Password: ")

strength = 0

chars = list(password)
if any(char.islower() for char in chars):
    strength += 1

chars1 = list(password)
if any(char.isupper() for char in chars):
    strength += 1

chars2 = list(password)
if any(char.isdigit() for char in chars):
    strength += 1

special_chars = ['!','@','#','$','%','^','&','*','(',')','_','+','-','=','[',']','{','}','|',';',':',',','.','<','>','?']
if any(char in special_chars for char in chars):
    strength += 1

if len(password) >= 8:
    strength += 1


(f"Your strength Index is:")
(str(strength))

if (strength) == 1 or strength == 2:
    print(f"Password Strength is Weak")

if (strength) == 3:
   print(f"Password Strength is Mid ")

if (strength) == 4:
   print(f"Password Strength is strong")

if (strength) == 5:
   print(f"Password Strength is super strong")

