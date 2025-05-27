import random 
jackpot = random.randint(1,100)
# print(jackpot)

guess = int(input("chal guess kar: "))
count = 1
while(guess!= jackpot):
    if(guess<jackpot):
        print("guess higher")
    else: 
        print("guess  lower")
    
    guess =int(input("chal guess kar: "))
    count +=1

print("sahi jawab")
print("you took ",count, "Attempts")
    
