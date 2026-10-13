# LCC ecsape room 1

code = "duck duck goose"
tries = 0
print("you are traped in a room guess to code to ecsape you have 10 tries. good luck.")

while True:
        guess = (input("Guess the code: "))
        if guess == code:
            print("Congrats,you escaped.")
            break
        if tries == 0:
                print("Incorrect! Hint: it is a popular party game.")
                print(f"You have used {tries} of your 10 tries. Be careful")
                tries += 1
        elif tries == 1:
                print("Incorrect! Hint: it is 3 words.")
                print(f"You have used {tries} of your 10 tries. Be careful")
                tries += 1
        elif tries == 2:
                print("incorect code here is a hint: all 3 words are amimal names")
                print(f"You have used {tries} of your 10 tries. Be careful")
                tries += 1
        elif tries == 3:
               print("Incorrect! Hint: word 1 and 2 are the same.")
               print(f"You have used {tries} of your 10 tries. Be careful")
               tries += 1
        elif tries == 4:
               print("Incorrect! Hint: all of the words are bird names.")
               print(f"You have used {tries} of your 10 tries. Be careful")
               tries += 1
        elif tries == 5:
                print("Incorrect! Hint: all of the words are aquatic bird names.")
                print(f"You have used {tries} of your 10 tries. Be careful") 
                tries += 1    
        elif tries == 6:
               print("Incorrect! Hint: quack quack honk.")
               print(f"You have used {tries} of your 10 tries. Be careful")
               tries += 1
        elif tries == 7:
               print("Incorrect! Hint: word 3 is a bigger bird that word 1 and 2.")
               print(f"You have used {tries} of your 10 tries. Be careful")
               tries += 1
        elif tries == 8:
               print("Incorrect! Hint: word 1 and 2 are common birds.")
               print(f"You have used {tries} of your 10 tries. Be careful")
               tries += 1
        elif tries == 9:
               print("Incorrect! Hint: an water version of this game is drip drip drop.")
               print(f"You have used {tries} of your 10 tries. Be careful")
               tries += 1
        elif tries == 10 :
               print("Incorrect! the code was duck duck goose.")
               print(f"You have used {tries} of your 10 tries. you failed. have fun rotting in this room forever")
        else:
               break 