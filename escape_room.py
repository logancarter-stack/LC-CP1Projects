# LCC ecsape room 1

code = "duckduckgoose"
tries = 0
print("you are trapped in a room guess to code to escape you have 10 tries. good luck.")

while True:
        guess = (input("Guess the code: "))
        if guess == (code.lower):
            print("Congrats,you escaped.")
            break
        tries += 1
        if tries == 1:
                print("Incorrect! Hint: it is a popular party game.")
                print(f"You have used {tries} of your 10 tries. Be careful")
        elif tries == 2:
                print("Incorrect! Hint: it is 3 words.")
                print(f"You have used {tries} of your 10 tries. Be careful")
        elif tries == 3:
                print("incorect code here is a hint: all 3 words are animal names")
                print(f"You have used {tries} of your 10 tries. Be careful")
        elif tries == 4:
               print("Incorrect! Hint: word 1 and 2 are the same.")
               print(f"You have used {tries} of your 10 tries. Be careful")
        elif tries == 5:
               print("Incorrect! Hint: all of the words are bird names.")
               print(f"You have used {tries} of your 10 tries. Be careful")
        elif tries == 6:
                print("Incorrect! Hint: all of the words are aquatic bird names.")
                print(f"You have used {tries} of your 10 tries. Be careful") 
        elif tries == 7:
               print("Incorrect! Hint: quack quack honk.")
               print(f"You have used {tries} of your 10 tries. Be careful")
        elif tries == 8:
               print("Incorrect! Hint: word 3 is a bigger bird that word 1 and 2.")
               print(f"You have used {tries} of your 10 tries. Be careful")
        elif tries == 9:
               print("Incorrect! Hint: word 1 and 2 are common birds.")
               print(f"You have used {tries} of your 10 tries. Be careful")
        elif tries == 10:
               print("Incorrect! Hint: a water version of this game is drip drip drop(no spaces).")
               print(f"You have used all of your 10 tries but im a nice guy so heres a extra try.")
        elif tries == 11 :
               print("Incorrect! the code was duckduckgoose.")
               print(f"You have used all of your 10 tries plus your bonus try. you failed. have fun rotting in this room forever")
        else:
               break

             