# print("while loop example")
# counter=1
# while counter<=5:
#     print("count", counter)
#     counter=counter+1

# print("counnt down for the happy new year")
# countdown=10
# print("Get ready everyone, the new year begins in 3...2...1...NOW")
# while countdown>0:
#     print(countdown)
#     countdown=countdown-1
# print("HAPPY NEW YEAR !!!")

# a=int(input("welcome to guess the number!"))

# if a > 18:
#     print("Too high")

# elif a < 18:
#     print("Too low")

# else:
#     print("Corret !!!")

print("welcome to guess the number!")
import random
secretnumber=random.randint(1,50)
guesscount=0
print("Try and guess the number 1 to 50 for prizes")
while True:
    guess=int(input("Enter your guess:  "))
    guesscount=guesscount+1
if guess == secretnumber:
    print("Corret !!!")
    "break"
elif guess < secretnumber:
    print("Too Low")

else:
    print("Too High")