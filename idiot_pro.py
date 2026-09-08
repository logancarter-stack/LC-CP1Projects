#logan carter idiot proof
print("Hello idiot.   I mean user!")

name=input("what is your name: ").strip().title()

print(f"Hello {name}")

while True:
    try:
        phone=int(input("what is your phone number: "))
    except:
        print("hey stupid that\'s not a number.")
    else:
        break    
print(f"calling {phone}")
print("Ring ring ring Ring ring ring Ring ring ring")
print(f"*over phone* hello is this {name} ?")