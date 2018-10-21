import random
secretnumber = random.randint(1,20)
name = input("Whats your name: ")
print("Hello "+name +" : Guess my number 1 to 20")

for guesstaken in range(1,7):
    guess = input("Enter number: ")
    if int(guess) > secretnumber:
        print ("Your number is too high")
    elif int(guess) < secretnumber:
        print("Your number is too low")
    else:
        break
    
if int(guess) == secretnumber:
    print("Congrats " +name ,"you guess my number in "+ str(guesstaken) + " times")
else:
    print("Nope you failed, My number was "+ str(secretnumber))
